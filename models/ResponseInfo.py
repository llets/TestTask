from dataclasses import dataclass


@dataclass
class ResponseInfo:

    url: str = None
    status_code: int = None
    fail: bool = None
    response_time: float = 0.0
    error_message: str = None

    def __str__(self):
        return (f"{self.url} "
                f"status_code: {self.status_code}, "
                f"fail: {self.fail}, "
                f"response_time: {self.response_time}, "
                f"error_message: {self.error_message}")