# encoding: utf-8

from flask import Flask
from best_app.modules import hello, goodbye
from best_app.config import CoolConfig


def create_app():    
    app = Flask(__name__)        
    app.config.from_mapping(
        SECRET_KEY = "My_Secret_Key"
    )     
    
    app.config.from_object(CoolConfig)    

    app.register_blueprint(hello.blueprint)
    app.register_blueprint(goodbye.blueprint)

    return app