import argparse

from constants.StringConstants import StringConstants
from keys.BaseKeyWithRegexValidation import BaseKeyWithRegexValidation
from utils.SplitUtil import SplitUtil
from utils.TypeUtil import TypeUtil


class HostsKey(BaseKeyWithRegexValidation):

    def __init__(self, config: dict):
        super().__init__(config)

    def add_to_parser(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(*self.keys,
                            help=self.description,
                            type=TypeUtil.get_type(self.type))

    def validate(self, value) -> bool:
        hosts = [host.strip() for host in SplitUtil.split_string(value, StringConstants.COMMA)]
        return all(self.regex.match(host) for host in hosts)