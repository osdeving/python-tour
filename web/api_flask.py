from flask import jsonify
from app import app

@app.route('/api/ping')
def ping():
    return jsonify({'message': 'pong'})
