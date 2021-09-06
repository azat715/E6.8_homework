from fastapi import FastAPI

from app import get_logger

logger = get_logger.get(__name__)

app = FastAPI()

async def fib(k: int) -> int:
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


@app.get("/fib/")
async def get_fib(k: int):
    """API вычисление числа Фиббаначи

    Args:
        k (int): Query parameter

    Returns:
        json: {"fib": "results"}
    """
    logger.info("Запуск api fib")
    results = await fib(k)
    return {"fib": results}