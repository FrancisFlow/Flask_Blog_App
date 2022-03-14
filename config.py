import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos' 
    SQL_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://francis:Master@localhost/blog'
    SECRET_KEY='FORTHELOVEofMoney'
class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://francis:Master@localhost/blog'

class ProdConfig(Config):
    pass
class TestConfig(Config):
    pass

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}