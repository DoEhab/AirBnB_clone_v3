#!/usr/bin/python3
"""this city class file handle rest API"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def get_states_by_id(state_id):
    """get state by id"""
    result = storage.get('State', state_id)
    if result is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(result.to_json())

    if request.method == 'DELETE':
        result.delete()
        del result
        return {}, 200

    if request.method == 'PUT':
        result = request.get_json()
        if result is None:
            abort(400, 'Not a JSON')


@app_views.route('/states', methods=['GET', 'POST'])
def get_states():
    """get all states"""
    if request.method == 'GET':
        return jsonify(storage.all('State').to_dict())

    if request.method == 'POST':
        result = request.get_json()
        if result is None:
            abort(400, 'Not a JSON')
        if result.get("name") is None:
            abort(400, 'Missing name')
