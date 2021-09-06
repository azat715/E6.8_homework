import pytest
from pathlib import Path

from logger import Level, LoggerConfigError, Logger

@pytest.fixture(name="logger")
def fixture_logger(set_env):
    get_logger = Logger()
    return get_logger.get("test")

def test_level(set_env):
    valid = Level(log_level="CRITICAL")
    assert valid.label == "CRITICAL"
    assert valid.value == 50
    with pytest.raises(LoggerConfigError) as excinfo:
        Level(log_level="unknown")
    assert str(excinfo.value) == "Неизвестный уровень логгирования: unknown"

def test_logger_env_invalid(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL", "INFO")
    with pytest.raises(LoggerConfigError) as excinfo:
        Logger()
    assert "Проверьте настройки evinoment. Отсутствует поле: ('LOG_FILE',)" == str(excinfo.value)

def test_logger_StreamHandler(logger):
    assert logger.level == 20
    assert logger.name == "test"
    logger.info("test_message1")


def test_logger_FileHandler(tmp_path, set_env):
    log_file = Path(tmp_path / "log_file.txt")
    get_logger = Logger()
    get_logger.file = log_file
    logger = get_logger.get("test", file=True)
    logger.info("test_message2")
    assert log_file.exists()

