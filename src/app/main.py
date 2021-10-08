from os import environ as env
from fastapi import FastAPI

from app import get_logger
from .base import Key, Cache
from redis_client import RedisClient, RedisConfig

file = bool(env.get("LOG_SAVE_FILE", False))

logger = get_logger.get(__name__)

app = FastAPI()

def fib(k: int) -> int:
    """Вычисление числа Фиббаначи

    Args:
        k (int): n-число 

    Returns:
        int: результат
    """
    logger.info("Вычисление числа fib")

    a: int = 0
    b: int = 1
    for _ in range(k):
        a, b = b, a + b
    return a

def connect_redis():
    config = RedisConfig.get_config()
    return RedisClient(config)

@app.get("/fib/")
async def get_fib(k: int):
    """API вычисление числа Фиббаначи

    Args:
        k (int): Query parameter

    Returns:
        json: {"fib": "results"}
    """
    logger.info("Запуск api fib")
    key = Key(str(k))
    r: Cache = connect_redis()
    if await r.is_exist(key):
        results = await r.get(key)
        logger.info("Значение {0} получено из redis".format(results))
    else:
        results = fib(k)
        if await r.set(key, results):
            logger.info("Значение {0} c ключом {1} сохранено в redis".format(results, k))
    return {"fib": results}