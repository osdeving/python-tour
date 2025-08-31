# Cookies e sessões em Flask
from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'segredo'
@app.route('/set')
def set_session():
    session['user'] = 'Ana'
    return 'Sessão definida!'
@app.route('/get')
def get_session():
    return f"Usuário: {session.get('user')}"
if __name__ == "__main__":
    app.run(debug=True)
