from dataclasses import dataclass, field
from statistics import mean
from typing import List

@dataclass
class HostStatistics:

    url: str = None
    success_count: int = 0
    fail_count: int = 0
    error_count: int = 0
    response_time: List[float] = field(default_factory=list)

    @property
    def total_count(self):
        return self.success_count + self.fail_count + self.error_count

    @property
    def min_time(self):
        return min(self.response_time) if self.response_time else 0.0

    @property
    def max_time(self):
        return max(self.response_time) if self.response_time else 0.0

    @property
    def avg_time(self):
        return mean(self.response_time) if self.response_time else 0.0

    def __str__(self):
        response_times_str = ', '.join(str(rt) for rt in self.response_time) if self.response_time else '[]'
        return (f"{self.url} "
                f"success_count: {self.success_count}, "
                f"fail_count: {self.fail_count}, "
                f"error_count: {self.error_count}, "
                f"(response_time: {response_times_str}) ")