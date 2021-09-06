class RedisConfigError(Exception):
    def __init__(self, message: str, field: str = None) -> None:
        self.field = field
        self.message = message
        super().__init__(self.message)