from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



#instantiating extentions
bootstrap=Bootstrap()
db=SQLAlchemy()

def create_app():

    app=Flask(__name__)


    #initializing flask extentions
    bootstrap.init_app(app)
    db.init_app(app)

    return app