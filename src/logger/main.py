from __future__ import annotations

import logging
from os import environ as env
from pathlib import Path
from typing import Optional, TypedDict

from .helper import Level, LoggerConfigError

class Logger():
    """Создание логгера
    """
    _log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

    def __init__(self, level: str) -> None:
        self.level = Level(log_level=level)

    @classmethod
    def config_from_env(cls) -> Logger:
        try:
            level = (env["LOG_LEVEL"])
        except KeyError as err:
            raise LoggerConfigError(message="Проверьте настройки evinoment. Отсутствует поле: {0}".format(err.args), field=str(err.args))
        else:
            return cls(level)
        

    def get_file_handler(self, file) -> logging.FileHandler:
        file_handler = logging.FileHandler(file)
        file_handler.setFormatter(logging.Formatter(self._log_format))
        return file_handler

    def get_stream_handler(self) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(self._log_format))
        return stream_handler


    def get(self, name, file: Optional[str] = None) -> logging.Logger:
        """Создание логгера

        Args:
            name (str): имя
            file (str, optional): Путь к логу.

        Returns:
            [Logger]: экземляр logging.Logger
        """
        logger = logging.getLogger(name)
        logger.setLevel(self.level.value)
        if file:
            logger.addHandler(self.get_file_handler(file))
        logger.addHandler(self.get_stream_handler())
        return logger


