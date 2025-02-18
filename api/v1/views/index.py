#!/usr/bin/python3
from api.v1.views import app_views
from flask import request, jsonify


@app_views.route('/status', method=['GET'])
def get_status():
    """Get method to return status"""
    if request.method == 'GET':
        response = {"status": "OK"}
        return jsonify(response)
