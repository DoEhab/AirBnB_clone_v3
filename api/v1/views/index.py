from api.v1.views import app_view
from flask import request, jsonify


@app_view.route('/status', method=['GET'])
def get_status():
    """Get method to return status"""
    if request.method == 'GET':
        response = {"status": "OK"}
        return jsonify(response)
