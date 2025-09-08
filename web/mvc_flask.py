# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "flask",
# ]
# ///

# Estrutura MVC em Flask
# Model
class User:
    def __init__(self, username):
        self.username = username
# Controller
from flask import Flask, render_template_string
app = Flask(__name__)
@app.route('/user/<username>')
def user_profile(username):
    user = User(username)
    return render_template_string('<h1>Usuário: {{ user.username }}</h1>', user=user)
# View: template inline acima
if __name__ == "__main__":
    app.run(debug=True)
