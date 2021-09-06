import pytest
from starlette.testclient import TestClient

@pytest.fixture(name="client")
def fixture_client(set_env):
    from app.main import app
    client = TestClient(app)
    return client


def test_fib(client, env_app):
    """Проверка работы get fib
    вроде бы в aioredis ошибка и если закешировать то возвращается строка а не int
    """
    payload = {'k': 10}
    response = client.get("/fib", params=payload)
    assert response.status_code == 200
    assert response.json() == {"fib": 55}