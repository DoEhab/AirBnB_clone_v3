#!/usr/bin/python3
""" start a flask web page """

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os

app = Flask(__name__)

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(exception):
    """close connection"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handle not found error"""
    response = {"error": "not found"}
    return jsonify(response), 404


if __name__ == "__main__":
    """entry point"""
    app.run(host=host, port=port)
