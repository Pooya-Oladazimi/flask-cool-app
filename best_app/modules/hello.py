# encoding: utf-8

from flask import Blueprint



blueprint = Blueprint('hello', __name__, url_prefix='/hello')


@blueprint.route("/say", methods=["GET"])
def say_hello():
    return "Hello!"