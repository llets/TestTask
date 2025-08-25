import argparse


class ParserUtil:

    NAME = "Console program for testing server availability over the HTTP protocol"

    @staticmethod
    def get_parser(keys) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(ParserUtil.NAME)

        for key in keys:
            key.add_to_parser(parser)

        return parser