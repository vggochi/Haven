
import httpx

from fastapi import HTTPException

from app.config import (
    SUPABASE_URL,
    SUPABASE_PUBLISHABLE_KEY
)


async def supabase_request(
    method: str,
    path: str,
    token: str | None = None,
    params: dict | None = None,
    json: dict | list | None = None,
    prefer: str | None = None
):
    # Verifica as configurações
    if not SUPABASE_URL:
        raise HTTPException(
            status_code=500,
            detail="SUPABASE_URL não foi configurada no .env."
        )

    if not SUPABASE_PUBLISHABLE_KEY:
        raise HTTPException(
            status_code=500,
            detail="SUPABASE_PUBLISHABLE_KEY não foi configurada no .env."
        )

    # Evita barras duplicadas na URL
    base_url = SUPABASE_URL.rstrip("/")
    endpoint = "/" + path.lstrip("/")

    url = f"{base_url}{endpoint}"

    headers = {
        "apikey": SUPABASE_PUBLISHABLE_KEY,
        "Content-Type": "application/json"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"
    else:
        headers["Authorization"] = (
            f"Bearer {SUPABASE_PUBLISHABLE_KEY}"
        )

    if prefer:
        headers["Prefer"] = prefer

    try:
        async with httpx.AsyncClient(
            timeout=httpx.Timeout(20.0, connect=10.0)
        ) as client:

            response = await client.request(
                method=method.upper(),
                url=url,
                headers=headers,
                params=params,
                json=json
            )

        # Tratamento de erros retornados pelo Supabase
        if response.status_code >= 400:
            try:
                error = response.json()

                message = (
                    error.get("message")
                    or error.get("msg")
                    or error.get("error_description")
                    or error.get("error")
                    or str(error)
                )

            except ValueError:
                message = response.text

            print(
                f"[SUPABASE ERROR] "
                f"Status: {response.status_code} "
                f"Mensagem: {message}"
            )

            raise HTTPException(
                status_code=response.status_code,
                detail=f"Erro do Supabase: {message}"
            )

        # Respostas sem conteúdo
        if response.status_code == 204 or not response.content:
            return None

        # Resposta JSON
        try:
            return response.json()
        except ValueError:
            return response.text

    except httpx.TimeoutException as error:
        print(f"[SUPABASE TIMEOUT] {error}")

        raise HTTPException(
            status_code=504,
            detail="O Supabase demorou demais para responder."
        )

    except httpx.RequestError as error:
        print(f"[SUPABASE CONNECTION ERROR] {repr(error)}")

        raise HTTPException(
            status_code=503,
            detail="Falha de comunicação com o Supabase. Verifique a URL e a conexão."
        ) from error
