from __future__ import annotations
from os import environ as env
from dataclasses import dataclass, fields

from .helper import RedisConfigError

@dataclass
class RedisConfig:
    """Настройки redis
    """
    host: str
    port: str = "6379"
    db: str = "0"


    def __post_init__(self):
        """Валидация

        Raises:
            Exception: Если поле равно None
        """
        for field in fields(self):
            if field is None:
                raise RedisConfigError(message="Ошибка: Поле {0} равно None".format(field), field=field)
        for field in ["port", "db"]:
            try:
                print(field)
                int(getattr(self, field))
            except ValueError:
                raise RedisConfigError(message="Ошибка: Поле {0} должно быть int".format(field), field=field)

    def __str__(self) -> str:
        """Форматирование url

        Returns:
            str: URL
        """
        return "redis://{self.host}:{self.port}/{self.db}".format(self=self)

    @classmethod
    def get_config(cls) -> RedisConfig:
        """Чтение настроек redis из environment

        Raises:
            Exception: Если нет ключа

        Returns:
            [cls]: RedisConfig
        """
    
        try:
            config = cls(host=env["REDIS_HOST"], port=env["REDIS_PORT"], db=env["REDIS_DB"])
        except KeyError as err:
            raise RedisConfigError("Проверьте настройки evinoment. Отсутствует поле: {0}".format(err.args), field=err.args)
        else:
            return config