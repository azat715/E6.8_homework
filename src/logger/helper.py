import logging
from dataclasses import InitVar, dataclass
from typing import ClassVar, List

class LoggerConfigError(Exception):
    def __init__(self, message: str, field: str = None) -> None:
        self.field = field
        self.message = message
        super().__init__(self.message)


@dataclass
class Level():
    log_level: InitVar[str]
    const_level: ClassVar[List[str]] = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]

    def __post_init__(self, log_level):
        """Валидация

        Raises:
            ValueError: Неизвестный уровень логгирования
        """
        if log_level not in self.const_level:
            raise LoggerConfigError(message="Неизвестный уровень логгирования: {0}".format(log_level), field=log_level)
        self.label = log_level
        self.value = getattr(logging, self.label)