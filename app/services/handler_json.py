import json
import os


class DecoderFile:

    @staticmethod
    def unpacking_json(file: str) -> dict | list[dict]:
        """
        Принимает строку с адресом расположения файла
        :param file:
        :return: tuple[type(), file]
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "..", "db", os.path.basename(file))
        with open(path, encoding='utf-8') as file:
            file = json.load(file)

        return file
