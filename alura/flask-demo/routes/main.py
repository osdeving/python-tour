from flask import Blueprint, jsonify

bp = Blueprint('bp', __name__)

@bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Realizar login do usuário"})


@bp.route('/products', methods=['GET'])
def products():
    return jsonify({"message": "List of products"})
