import pytest

@pytest.fixture(name="set_env")
def fixture_set_env(monkeypatch):
    monkeypatch.setenv("LOG_FILE", "test_log_file")
    monkeypatch.setenv("LOG_LEVEL", "INFO")


@pytest.fixture(name="env_redis")
def fixture_env_redis(monkeypatch):
    monkeypatch.setenv("REDIS_HOST", "localhost")
    monkeypatch.setenv("REDIS_PORT", "8000")
    monkeypatch.setenv("REDIS_DB", "1")