import json
import logging

from exceptions.InvalidKeyValueException import InvalidKeyValueException
from keys.BaseKey import BaseKey
from utils.KeyFactory import KeyFactory
from utils.PathUtil import PathUtil


class KeyLoader:

    @staticmethod
    def get_keys_info(config_file="configuration.json") -> [BaseKey]:
        file_path = PathUtil.get_resource_path(config_file)
        logging.debug(f"Getting key info from file {file_path}")
        keys = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                keys_data = json.load(f)

            for key_info in keys_data:
                key = KeyFactory.create_key(key_info)
                keys.append(key)

            return keys

        except FileNotFoundError as e:
            logging.error(f"File ${file_path} wasn't found. Couldn't load keys' information.")
            raise e
        except json.JSONDecodeError as e:
            logging.error(f"Error parsing json keys' configuration from ${file_path}.")
            raise e
        except Exception as e:
            logging.error(f"Error loading keys from ${file_path}.")
            raise e

    @staticmethod
    def validate_parsed_args(parsed_args, loaded_keys) -> None:
        logging.debug('Validating parsed args')
        all_valid = True
        message = ''

        for key in loaded_keys:

            value = getattr(parsed_args, key.name, None)

            if value is not None:
                exclusives = getattr(key, 'exclusive_with', [])
                for exclusive in exclusives:
                    exclusive_value = getattr(parsed_args, exclusive, None)
                    if exclusive_value is not None:
                        raise InvalidKeyValueException(
                            f"Only one of the keys can be specified at a time '{key.name}' or '{exclusive}'"
                        )
                if not key.validate(value):
                    message += f"Invalid value for {key.name}: {value}"
                    all_valid = False
            else:
                exclusives = getattr(key, 'exclusive_with', [])
                for exclusive in exclusives:
                    exclusive_value = getattr(parsed_args, exclusive, None)
                    if exclusive_value is None:
                        raise InvalidKeyValueException(
                            f"One of the keys should be specified at a time: either '{key.name}' or '{exclusive}'")
        if not all_valid:
            raise InvalidKeyValueException(message)