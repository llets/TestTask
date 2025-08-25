from models.HostStatistics import HostStatistics


class StatisticsUtil:

    @staticmethod
    def print_results(statistics: dict[str, HostStatistics]) -> None:
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