from exceptions.InvalidKeyException import InvalidKeyException
from keys.BaseKey import BaseKey
from keys.CountKey import CountKey
from keys.HostsKey import HostsKey

class KeyFactory:

    @staticmethod
    def create_key(config: dict) -> BaseKey:
        key_name = config['name']
        match key_name:
            case "hosts":
                return HostsKey(config)
            case "count":
                return CountKey(config)
            case _:
                raise InvalidKeyException("Invalid key was entered in console!")