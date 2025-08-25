class ResponseCodeUtil:

    @staticmethod
    def is_failed(status_code: int) -> bool:
        return True if status_code == 400 or status_code == 500 else False