import argparse
from abc import ABC, abstractmethod


class BaseKey(ABC):

    name: str
    type: str
    keys: list
    description: str

    def __init__(self, config: dict):
        self.name = config['name']
        self.type = config['type']
        self.keys = config['keys']
        self.description = config['description']

    @abstractmethod
    def add_to_parser(self, parser: argparse.ArgumentParser) -> None:
        pass

    @abstractmethod
    def validate(self, value) -> bool:
        pass

    def __str__(self):
        return (f"{self.name} "
                f"(keys: '{', '.join(self.keys)}', "
                f"type: {self.type}, "
                f"description: '{self.description}')")