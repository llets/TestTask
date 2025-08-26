import logging


class StringUtil:

    @staticmethod
    def split_string(string: str, splitter: str) -> [str]:
        logging.debug(f'Splitting string {string}')
        return string.split(splitter)