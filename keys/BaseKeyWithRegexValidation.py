import re
from abc import ABC

from keys.BaseKey import BaseKey


class BaseKeyWithRegexValidation(BaseKey, ABC):

    regex: re.Pattern

    def __init__(self, config: dict):
        super().__init__(config)
        self.regex = re.compile(config["regex_pattern"])