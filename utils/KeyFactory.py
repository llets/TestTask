import logging

from exceptions.InvalidKeyException import InvalidKeyException
from keys.BaseKey import BaseKey
from keys.CountKey import CountKey
from keys.FileKey import FileKey
from keys.HostsKey import HostsKey
from keys.OutputKey import OutputKey


class KeyFactory:

    @staticmethod
    def create_key(config: dict) -> BaseKey:
        key_name = config['name']
        logging.debug(f"Creating key object for {key_name}")
        match key_name:
            case "hosts":
                return HostsKey(config)
            case "count":
                return CountKey(config)
            case "file":
                return FileKey(config)
            case "output":
                return OutputKey(config)
            case _:
                raise InvalidKeyException("Invalid key was entered in console!")