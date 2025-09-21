from flask import Blueprint, jsonify

bp = Blueprint('bp', __name__)

@bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Realizar login do usuário"})


@bp.route('/products', methods=['GET'])
def get_products():
    return jsonify({"message": "List of products"})

@bp.route('/products/<int:product_id>', methods=['GET'])
def get_product():
    return jsonify({'message:'})