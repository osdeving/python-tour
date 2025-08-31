from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/resource', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def resource():
    if request.method == 'GET':
        return jsonify({'method': 'GET', 'status': 200}), 200
    elif request.method == 'POST':
        return jsonify({'method': 'POST', 'status': 201}), 201
    elif request.method == 'PUT':
        return jsonify({'method': 'PUT', 'status': 200}), 200
    elif request.method == 'DELETE':
        return jsonify({'method': 'DELETE', 'status': 204}), 204
    elif request.method == 'PATCH':
        return jsonify({'method': 'PATCH', 'status': 200}), 200

if __name__ == "__main__":
    app.run(debug=True)

# Para testar: python web/http_rest.py
# Teste com curl ou Postman usando diferentes métodos HTTP
