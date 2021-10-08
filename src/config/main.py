

class Logger(object):
    _instance = None

    fields = ["REDIS_HOST", "REDIS_PORT", "REDIS_DB", "LOG_FILE", "LOG_LEVEL"]

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance