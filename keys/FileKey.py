import argparse
import logging

from keys.BaseKey import BaseKey
from utils.TypeUtil import TypeUtil


class FileKey(BaseKey):

    def __init__(self, config: dict):
        super().__init__(config)

    def add_to_parser(self, parser: argparse.ArgumentParser) -> None:
        logging.debug("Adding File key to parser")
        parser.add_argument(*self.keys,
                            help=self.description,
                            type=TypeUtil.get_type(self.type))

    def validate(self, value) -> bool:
        logging.debug("Validating File key value")
        if isinstance(value, str):
            return True