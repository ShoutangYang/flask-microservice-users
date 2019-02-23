
class BaseConfig:
    DEBUG=False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    BEBUG=True
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG=False

