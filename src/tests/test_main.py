import pytest
from starlette.testclient import TestClient

@pytest.fixture(name="client")
def fixture_client(set_env):
    from app.main import app
    client = TestClient(app)
    return client


def test_fib(client):
    """Проверка работы get fib
    """
    payload = {'k': '10'}
    response = client.get("/fib", params=payload)
    assert response.status_code == 200
    assert response.json() == {"fib": 55}