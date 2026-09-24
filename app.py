from flask import Flask, redirect, url_for
from routes.user_routes import app as user_routes

app = Flask(__name__)
app.register_blueprint(user_routes)


@app.route('/')
def index():
    return redirect(url_for('user.listar_tarefas'))


if __name__ == '__main__':
    app.run(debug=True)
