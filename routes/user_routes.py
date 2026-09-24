from services import user_service
from flask import request, redirect, url_for, render_template, Blueprint

app = Blueprint("user", __name__)


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = user_service.listar()
    return render_template('listar_tarefas.html', tarefas=tarefas)


@app.route('/tarefas/cadastrar', methods=['POST'])
def cadastrar_tarefa():
    nome = request.form['nome']
    user_service.cadastrar(nome)
    return redirect(url_for('user.listar_tarefas'))


@app.route('/tarefas/editar/<int:id>', methods=['POST'])
def editar_tarefa(id):
    nome = request.form['nome']
    status = request.form.get('status') == 'on'
    user_service.editar(id, nome, status)
    return redirect(url_for('user.listar_tarefas'))


@app.route('/tarefas/excluir/<int:id>', methods=['POST'])
def excluir_tarefa(id):
    user_service.excluir(id)
    return redirect(url_for('user.listar_tarefas'))


@app.route('/tarefas/aprovar/<int:id>', methods=['POST'])
def aprovar_tarefa(id):
    user_service.aprovar(id)
    return redirect(url_for('user.listar_tarefas'))


@app.route('/tarefas/reprovar/<int:id>', methods=['POST'])
def reprovar_tarefa(id):
    user_service.reprovar(id)
    return redirect(url_for('user.listar_tarefas'))
