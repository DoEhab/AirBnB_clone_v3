#!/usr/bin/python3
"""this file contains API routes"""

from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """Get method to return status"""
    if request.method == 'GET':
        response = {"status": "OK"}
        return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Get method to return status"""
    if request.method == 'GET':
        return jsonify(storage.count())
