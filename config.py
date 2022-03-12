import os

class Config:
    SQL_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    DEBUG=True
class ProdConfig(Config):
    pass
class TestConfig(Config):
    pass

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}