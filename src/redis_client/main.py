from typing import Union

import aioredis

from .config import RedisConfig
from .helper import Key

class RedisClient:
    def __init__(self, config: RedisConfig) -> None:
        self.config = str(config)
        self.r:aioredis.Redis = aioredis.from_url(self.config)

    async def set(self, key: Key, value) -> bool:
        res = await self.r.set(key, value)
        return res

    async def get(self, key) -> Union[str, int, None]:
        res = await self.r.get(key)
        if res:
            if isinstance(res, int):
                return res
            return res.decode("utf-8")
        else:
            return None

    async def is_exist(self, key: Key) -> bool:
        if await self.r.exists(key) == 1:
            return True
        return False
