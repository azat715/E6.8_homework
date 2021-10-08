from typing import Protocol, NewType, Union, Any
from abc import abstractmethod

Key = NewType('Key', str)

class Cache(Protocol):
    @abstractmethod
    async def set(self, key: Key, value: Any) -> bool:
        pass

    @abstractmethod
    async def get(self, key: Key) -> Union[str, int]:
        pass

    @abstractmethod
    async def is_exist(self, key: Key) -> bool:
        raise NotImplementedError("Метод не реализован в этом классе")


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]