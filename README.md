# Checklist TF

Aplicativo web simples para controlar tarefas e lista de pendências.

## Para que serve

Este projeto serve para:

- cadastrar tarefas;
- visualizar todas as tarefas em uma tela;
- marcar como concluída ou pendente;
- editar o nome e o status;
- excluir tarefas;
- salvar os dados no Supabase.

A interface foi feita com Flask e HTML, e a base de dados é usada via Supabase.

## Como baixar

Você pode baixar este projeto clonando o repositório:

```bash
git clone <url-do-repositorio>
cd Checklist_TF
```

Se você recebeu o código em ZIP, basta extrair a pasta e entrar nela.

## Como fazer funcionar

### 1. Instalar Python

Certifique-se de ter o Python instalado no computador.

### 2. Criar ambiente virtual

No terminal, dentro da pasta do projeto, execute:

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

O projeto usa Supabase. Verifique o arquivo `chaves.env` e preencha com seus dados:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
```

Também existe um arquivo chamado `exemplo.env` como modelo.

### 5. Rodar a aplicação

```bash
python app.py
```

Depois, abra no navegador:

```text
http://127.0.0.1:5000
```

A página inicial redireciona para a lista de tarefas.

## Estrutura principal

- `app.py` - inicia a aplicação
- `config.py` - conecta com o Supabase
- `routes/` - rotas da aplicação
- `services/` - regras de negócio
- `repository/` - acesso ao banco
- `templates/` - páginas HTML

## Observações

Se o projeto mostrar erro sobre variáveis de ambiente, verifique se o arquivo `chaves.env` existe e contém `SUPABASE_URL` e `SUPABASE_KEY` corretos.

Se a aplicação não abrir, confirme se todas as dependências foram instaladas e se o ambiente virtual está ativado.
