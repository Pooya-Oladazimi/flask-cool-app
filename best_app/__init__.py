# encoding: utf-8

from flask import Flask


def create_app():    
    app = Flask(__name__)        
    app.config.from_mapping(
        SECRET_KEY = "My_Secret_Key"
    )     
    
    return app