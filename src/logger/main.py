from __future__ import annotations

import logging
from os import environ as env

from .helper import Level, LoggerConfigError


class Logger():
    """Создание логгера
    """
    _log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

    def __init__(self) -> None:
        try:
            self.file = env["LOG_FILE"]   
            self.level = Level(log_level=env["LOG_LEVEL"])
        except KeyError as err:
            raise LoggerConfigError("Проверьте настройки evinoment. Отсутствует поле: {0}".format(err.args), field=err.args)

    def get_file_handler(self) -> logging.FileHandler:
            file_handler = logging.FileHandler(self.file)
            file_handler.setFormatter(logging.Formatter(self._log_format))
            return file_handler

    def get_stream_handler(self) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(self._log_format))
        return stream_handler


    def get(self, name, file: bool=False) -> logging.Logger:
        """Создание логгера

        Args:
            name (str): имя
            file (bool, optional): Создание файла лога. Defaults to False.

        Returns:
            [Logger]: экземляр logging.Logger
        """
        logger = logging.getLogger(name)
        logger.setLevel(self.level.value)
        if file:
            logger.addHandler(self.get_file_handler())
        logger.addHandler(self.get_stream_handler())
        return logger


