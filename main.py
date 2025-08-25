import logging

from constants.StringConstants import StringConstants
from utils.FileUtil import FileUtil
from utils.HttpUtil import HttpUtil
from utils.KeyLoader import KeyLoader
from utils.Parser import Parser
from utils.StatisticsUtil import StatisticsUtil
from utils.StringUtil import StringUtil

class RootFilter(logging.Filter):
    def filter(self, record):
        return record.name == 'root'

if __name__ == "__main__":

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.addFilter(RootFilter())
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    logging.info('Loading keys information')
    keys = KeyLoader.get_keys_info()

    logging.info('Creating parser and getting parsed arguments')
    parser = Parser(keys)
    parsed_args = parser.get_parsed_arguments()

    logging.info('Validating parsed arguments')
    KeyLoader.validate_parsed_args(parsed_args=parsed_args, loaded_keys=keys)

    logging.info('Testing servers')
    if parsed_args.hosts is not None:
        list_of_urls = StringUtil.split_string(parsed_args.hosts, StringConstants.COMMA)
        statistics = HttpUtil.test_server_availability(list_of_urls, parsed_args.count)
    else:
        list_of_urls = StringUtil.split_string(FileUtil.get_file_info(parsed_args.file), StringConstants.ENTER)
        statistics = HttpUtil.test_server_availability(list_of_urls, parsed_args.count)

    if parsed_args.output is None:
        logging.info('Printing statistics')
        StatisticsUtil.print_results(statistics)
    else:
        logging.info('Saving statistics into file')
        FileUtil.save_into_file(parsed_args.output, StatisticsUtil.get_results(statistics))