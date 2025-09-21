from flask import Blueprint, jsonify

bp = Blueprint('bp', __name__)

@bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Realizar login do usuário"})


@bp.route('/products', methods=['GET'])
def get_products():
    return jsonify({"message": "List of products"})

@bp.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return jsonify({'message': f"Retorna o produto de id = {product_id}"})

@bp.route('/products', methods=['POST'])
def create_product(product: Product):
    return jsonify({'message': f"Cria o produto {product.name}"})

@bp.route('/products/<int:product_id>', methods=['PUT'])
def create_product(product_id):
    return jsonify({'message': f"Cria o produto {product.name}"})
