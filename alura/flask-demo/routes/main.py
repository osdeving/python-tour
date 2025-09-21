from flask import Blueprint, jsonify

bp = Blueprint('bp', __name__)

@bp.route('/login', methods['POST'])
def login():
    