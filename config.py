import os

from dotenv import load_dotenv
from supabase import Client, create_client

base_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base_dir, "chaves.env"))

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        "Variáveis de ambiente do Supabase não foram encontradas. "
        "Verifique o arquivo chaves.env e as chaves SUPABASE_URL/SUPABASE_KEY."
    )

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
