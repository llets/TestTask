import argparse
import logging
from argparse import Namespace


class Parser:

    NAME = "Console program for testing server availability over the HTTP protocol"

    def __init__(self, keys):
        self.parser = argparse.ArgumentParser(Parser.NAME)
        self.parsed_args = None
        for key in keys:
            key.add_to_parser(self.parser)

    def get_parsed_arguments(self) -> Namespace:
        logging.debug('Getting parsed arguments')
        if self.parsed_args is None:
            self.parsed_args = self.parser.parse_args()
        return self.parser.parse_args()