
import os
from pathlib import Path
from urllib.parse import urlparse

import httpx
from dotenv import load_dotenv


# Localiza o .env na pasta backend
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

print("\n========== DIAGNÓSTICO HAVEN ==========\n")

print("1. ARQUIVO .ENV")

print("Caminho:", ENV_FILE)
print("Existe:", ENV_FILE.exists())

load_dotenv(ENV_FILE, override=True)

SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip().rstrip("/")
SUPABASE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY", "").strip()

print("\n2. VARIÁVEIS")

print("SUPABASE_URL encontrada:", bool(SUPABASE_URL))
print("SUPABASE_KEY encontrada:", bool(SUPABASE_KEY))

if not SUPABASE_URL or not SUPABASE_KEY:
    print("\nFALHA: confira os nomes das variáveis no .env.")
    raise SystemExit(1)

parsed = urlparse(SUPABASE_URL)

print("\n3. URL DO PROJETO")
print("Protocolo:", parsed.scheme)
print("Domínio:", parsed.hostname)
print("Formato HTTPS:", parsed.scheme == "https")
print("Formato de domínio Supabase:",
      bool(parsed.hostname and parsed.hostname.endswith(".supabase.co")))

if parsed.scheme != "https" or not parsed.hostname:
    print("\nFALHA: a URL do Supabase parece estar incorreta.")
    raise SystemExit(1)

# Testa os serviços sem enviar a chave como token Bearer.
headers = {
    "apikey": SUPABASE_KEY
}

tests = [
    ("Auth Health", f"{SUPABASE_URL}/auth/v1/health"),
    ("REST API", f"{SUPABASE_URL}/rest/v1/")
]

print("\n4. TESTES DE CONEXÃO")

with httpx.Client(timeout=15, follow_redirects=True) as client:
    for name, endpoint in tests:
        print(f"\nTestando: {name}")

        try:
            response = client.get(endpoint, headers=headers)

            print("Status HTTP:", response.status_code)
            print("Resposta:", response.text[:500])

            if response.status_code < 400:
                print("RESULTADO: serviço respondeu.")
            elif response.status_code in (401, 403):
                print("RESULTADO: serviço acessível, mas houve rejeição de autenticação/permissão.")
            else:
                print("RESULTADO: serviço respondeu com erro HTTP.")

        except httpx.TimeoutException:
            print("FALHA: tempo limite excedido.")

        except httpx.ConnectError as error:
            print("FALHA DE CONEXÃO:", repr(error))

        except httpx.RequestError as error:
            print("ERRO DE REQUISIÇÃO:", repr(error))

print("\n========== FIM DO DIAGNÓSTICO ==========\n")
