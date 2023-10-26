# encoding: utf-8

from flask import Flask
from best_app.modules import hello, goodbye, user
from best_app.config import CoolConfig
from flask_migrate import Migrate
from best_app.database import db
from flask_cors import CORS


def create_app():    
    app = Flask(__name__)        
    app.config.from_mapping(
        SECRET_KEY = "My_Secret_Key"
    )     
    
    app.config.from_object(CoolConfig)    
    CORS(app, origins=['http://localhost:3000'])  

    db.init_app(app)
    from best_app.models.user import User
    from best_app.models.car import Car    
    migrate = Migrate(app, db)

    app.register_blueprint(hello.blueprint)
    app.register_blueprint(goodbye.blueprint)
    app.register_blueprint(user.blueprint)

    return app