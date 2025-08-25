import argparse
import logging

from constants.StringConstants import StringConstants
from keys.BaseKeyWithRegexValidation import BaseKeyWithRegexValidation
from utils.StringUtil import StringUtil
from utils.TypeUtil import TypeUtil


class HostsKey(BaseKeyWithRegexValidation):

    exclusive_with: list

    def __init__(self, config: dict):
        super().__init__(config)
        self.exclusive_with = config['exclusive_with']

    def add_to_parser(self, parser: argparse.ArgumentParser) -> None:
        logging.debug("Adding Hosts key to parser")
        parser.add_argument(*self.keys,
                            help=self.description,
                            type=TypeUtil.get_type(self.type))

    def validate(self, value) -> bool:
        logging.debug("Validating Hosts key value")
        hosts = [host.strip() for host in StringUtil.split_string(value, StringConstants.COMMA)]
        return all(self.regex.match(host) for host in hosts)

    def __str__(self):
        return (f"{self.name} "
                f"(keys: '{', '.join(self.keys)}', "
                f"type: {self.type}, "
                f"description: '{self.description}', "
                f"(exclusive_with: '{', '.join(self.exclusive_with)}')")