# Segurança Flask
from flask import Flask, request
import bcrypt
app = Flask(__name__)
@app.route('/xss')
def xss():
    nome = request.args.get('nome', '')
    # Proteja usando escape ou templates
    return f"Olá, {nome}"  # Vulnerável a XSS
@app.route('/hash')
def hash_senha():
    senha = b'segredo'
    hash = bcrypt.hashpw(senha, bcrypt.gensalt())
    return hash.decode()
if __name__ == "__main__":
    app.run(debug=True)
