#!/usr/bin/python3
"""this state file handle rest API"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE'])
def get_states_by_id():
    """get state by id"""
    storage.all('State')
    return None


@app_views.route('/states', methods=['GET', 'POST'])
def get_states():
    """get all states"""
    if request.method == 'GET':
        return jsonify(storage.all('State').to_dict())
