# encoding: utf-8

from flask import Blueprint, current_app


blueprint = Blueprint('hello', __name__, url_prefix='/hello')


@blueprint.route("/say", methods=["GET"])
def say_hello():
    return "Hello {}!".format(current_app.config.get('MY_ENV_VAR'))