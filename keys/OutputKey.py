import argparse
import logging

from keys.BaseKey import BaseKey
from utils.TypeUtil import TypeUtil


class OutputKey(BaseKey):

    def __init__(self, config: dict):
        super().__init__(config)

    def add_to_parser(self, parser: argparse.ArgumentParser) -> None:
        logging.debug("Adding Output key to parser")
        parser.add_argument(*self.keys,
                            help=self.description,
                            type=TypeUtil.get_type(self.type))

    def validate(self, value) -> bool:
        logging.debug("Validating Output key value")
        if isinstance(value, str):
            return True