import os

class Config:
     # simple mail transfer protocol server configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    UPLOADED_PHOTOS_DEST ='app/static/photos' 
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