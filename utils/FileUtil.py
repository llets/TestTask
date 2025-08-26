import logging

from utils.PathUtil import PathUtil


class FileUtil:

    @staticmethod
    def get_file_info(file_name: str) -> str:
        logging.debug(f"Getting info from file {file_name}")
        file_path = PathUtil.get_resource_path(file_name)
        try:
            with open(file_path, "r", encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError as e:
            logging.error(f'File {file_name} was not found.')
            raise e
        except Exception as e:
            logging.error(f'Unexpected exception: {e}')
            raise e

    @staticmethod
    def save_into_file(file_name: str, content: str) -> None:
        logging.debug(f"Saving info into file {file_name}")
        file_path = PathUtil.get_resource_path(file_name)
        try:
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            logging.error(f'Unexpected exception: {e}')
            raise e