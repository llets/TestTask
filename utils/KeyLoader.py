import json

from exceptions.InvalidKeyValueException import InvalidKeyValueException
from keys.BaseKey import BaseKey
from utils.KeyFactory import KeyFactory
from utils.PathUtil import PathUtil


class KeyLoader:

    @staticmethod
    def get_keys_info(config_file="configuration.json") -> [BaseKey]:

        file_path = PathUtil.get_resource_path(config_file)

        keys = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                keys_data = json.load(f)

            for key_info in keys_data:
                key = KeyFactory.create_key(key_info)
                keys.append(key)

            print(f"All keys are loaded from file ${file_path}")
            return keys

        except FileNotFoundError as e:
            print(f"File ${file_path} wasn't found. Couldn't load keys' information.")
            raise e
        except json.JSONDecodeError as e:
            print(f"Error parsing json keys' configuration from ${file_path}.")
            raise e
        except Exception as e:
            print(f"Error loading keys from ${file_path}.")
            raise e

    @staticmethod
    def validate_parsed_args(parsed_args, loaded_keys) -> None:
        all_valid = True
        message = ''

        for key in loaded_keys:

            value = getattr(parsed_args, key.name, None)

            if value is not None:
                if not key.validate(value):
                    message += f"Invalid value for {key.name}: {value}"
                    all_valid = False
            # elif key.required:
            #     print(f"Missing required argument: {key.name}")
            #     all_valid = False
        if not all_valid:
            raise InvalidKeyValueException(message)