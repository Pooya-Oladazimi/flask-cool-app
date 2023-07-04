# encoding: utf-8

from flask import Blueprint


blueprint = Blueprint('bye', __name__, url_prefix='/bye')


@blueprint.route("/say", methods=["GET"])
def say_bye():
    return "Goodbye!"