import logging


class StringUtil:

    @staticmethod
    def split_string(string, splitter):
        logging.debug(f'Splitting string {string}')
        return string.split(splitter)