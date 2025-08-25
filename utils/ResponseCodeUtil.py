import logging


class ResponseCodeUtil:

    @staticmethod
    def is_failed(status_code: int) -> bool:
        logging.debug('Checking if the status code is referred to failed or not')
        return True if status_code == 400 or status_code == 500 else False