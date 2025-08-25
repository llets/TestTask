import logging

from models.HostStatistics import HostStatistics


class StatisticsUtil:

    @staticmethod
    def print_results(statistics: dict[str, HostStatistics]) -> None:
        logging.debug('Printing server availability results')

        print("\n" + "=" * 50)
        print("TESTING SERVER AVAILABILITY RESULTS")
        print("=" * 50)

        for host, stats in statistics.items():
            stats: HostStatistics
            print(f"\nHost: {host}")
            print(f"  Total requests:   {stats.total_count}")
            print(f"  Successful:       {stats.success_count}")
            print(f"  Failed (400/500): {stats.fail_count}")
            print(f"  Errors:           {stats.error_count}")

            if stats.success_count + stats.fail_count > 0:
                print(f"  Min time:         {stats.min_time:.3f}s")
                print(f"  Max time:         {stats.max_time:.3f}s")
                print(f"  Avg time:         {stats.avg_time:.3f}s")
            else:
                print(f"  No suitable requests to calculate timing")

        print("\n" + "=" * 50)

    @staticmethod
    def get_results(statistics: dict[str, HostStatistics]) -> str:
        logging.debug('Getting server availability results')

        result = ''
        result += "\n" + "=" * 50
        result += "\nTESTING SERVER AVAILABILITY RESULTS"
        result += "\n" + "=" * 50

        for host, stats in statistics.items():
            stats: HostStatistics
            result +=  f"\nHost: {host}"
            result += f"\n  Total requests:   {stats.total_count}"
            result += f"\n  Successful:       {stats.success_count}"
            result += f"\n  Failed (400/500): {stats.fail_count}"
            result += f"\n  Errors:           {stats.error_count}"

            if stats.success_count + stats.fail_count > 0:
                result += f"\n  Min time:         {stats.min_time:.3f}s"
                result += f"\n  Max time:         {stats.max_time:.3f}s"
                result += f"\n  Avg time:         {stats.avg_time:.3f}s"
            else:
                result += f"\n  No suitable requests to calculate timing"

        result += "\n" + "=" * 50
        return result