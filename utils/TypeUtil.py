import logging


class TypeUtil:

    @staticmethod
    def get_type(type_str):
        logging.debug(f'Getting type for string {type_str}')
        type_map = {
            'str': str,
            'int': int
        }
        return type_map.get(type_str, str)