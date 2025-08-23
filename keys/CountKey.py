import argparse

from keys.BaseKey import BaseKey
from utils.TypeUtil import TypeUtil


class CountKey(BaseKey):

    default: int

    def __init__(self, config: dict):
        super().__init__(config)
        self.default = config['default']

    def add_to_parser(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(*self.keys,
                            help=self.description,
                            type=TypeUtil.get_type(self.type),
                            default=self.default)

    def validate(self, value) -> bool:
        if isinstance(value, int):
            return True