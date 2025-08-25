import os

class PathUtil:
    _BASE_DIR = os.path.dirname((os.path.dirname(__file__)))

    @staticmethod
    def get_resource_path(filename):
        return os.path.join(PathUtil._BASE_DIR, "resources", filename)