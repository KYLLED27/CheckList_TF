from config import supabase


def cadastrar_tarefa(nome: str, status: bool = False):
    data = {
        "nome": nome,
        "status": status
    }
    response = supabase.table("tarefas").insert(data).execute()
    return response.data


def editar_tarefa(id: int, nome: str, status: bool):
    data = {
        "nome": nome,
        "status": status
    }
    response = supabase.table("tarefas").update(data).eq("id", id).execute()
    return response.data


def excluir_tarefa(id: int):
    response = supabase.table("tarefas").delete().eq("id", id).execute()
    return response.data


def listar_tarefas():
    response = supabase.table("tarefas").select("*").order("id").execute()
    return response.data


def buscar_tarefa(id: int):
    response = supabase.table("tarefas").select("*").eq("id", id).single().execute()
    return response.data


def aprovar_tarefa(id: int):
    response = supabase.table("tarefas").update({"status": True}).eq("id", id).execute()
    return response.data


def reprovar_tarefa(id: int):
    response = supabase.table("tarefas").update({"status": False}).eq("id", id).execute()
    return response.data
