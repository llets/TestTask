from utils.HttpUtil import HttpUtil
from utils.KeyLoader import KeyLoader
from utils.ParserUtil import ParserUtil
from utils.StatisticsUtil import StatisticsUtil

if __name__ == "__main__":

    keys = KeyLoader.get_keys_info()
    parser = ParserUtil.get_parser(keys)
    parsed_args = parser.parse_args()

    KeyLoader.validate_parsed_args(parsed_args=parsed_args, loaded_keys=keys)

    statistics = HttpUtil.test_server_availability(parsed_args.hosts, parsed_args.count)

    for key, value in statistics.items():
        print(f"{value}")

    StatisticsUtil.print_results(statistics)