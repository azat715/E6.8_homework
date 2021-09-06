from typing import Union

import aioredis

from .config import RedisConfig

class RedisClient:
    def __init__(self, config: RedisConfig) -> None:
        self.config = config
        self.r:aioredis.Redis

    def connect(self) -> None:
        self.r = aioredis.from_url(self.config)

    async def set(self, key, value) -> bool:
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

    async def is_exist(self, key) -> bool:
        if await self.r.exists(key) == 1:
            return True
        return False
