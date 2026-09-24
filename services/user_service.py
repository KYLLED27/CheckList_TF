from repository import user_repository


def listar():
    return user_repository.listar_tarefas()


def buscar(id: int):
    return user_repository.buscar_tarefa(id)


def cadastrar(nome: str):
    return user_repository.cadastrar_tarefa(nome)


def editar(id: int, nome: str, status: bool = False):
    return user_repository.editar_tarefa(id, nome, status)


def excluir(id: int):
    return user_repository.excluir_tarefa(id)


def aprovar(id: int):
    return user_repository.aprovar_tarefa(id)


def reprovar(id: int):
    return user_repository.reprovar_tarefa(id)
