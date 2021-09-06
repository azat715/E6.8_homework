import pytest

from redis_client import RedisConfig, RedisConfigError

def test_valid_conf(env_redis):
    config = RedisConfig.get_config()
    assert config.host == "localhost"
    assert config.port == "8000"
    assert config.db == "1"
    assert str(config) == "redis://localhost:8000/1"

def test_invalid_conf(monkeypatch):
    with pytest.raises(RedisConfigError) as excinfo:
        RedisConfig.get_config()
    assert "Проверьте настройки evinoment. Отсутствует поле: ('REDIS_HOST',)" == str(excinfo.value)
    monkeypatch.setenv("REDIS_HOST", "localhost")
    monkeypatch.setenv("REDIS_PORT", "8000")
    monkeypatch.setenv("REDIS_DB", "no_int")
    with pytest.raises(RedisConfigError) as excinfo:
        RedisConfig.get_config()
    assert 'Ошибка: Поле db должно быть int' == str(excinfo.value)
