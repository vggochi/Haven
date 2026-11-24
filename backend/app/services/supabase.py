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
    headers = {
        "apikey": SUPABASE_PUBLISHABLE_KEY,
        "Content-Type": "application/json"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    if prefer:
        headers["Prefer"] = prefer

    try:
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.request(
                method=method,
                url=f"{SUPABASE_URL}{path}",
                headers=headers,
                params=params,
                json=json
            )

        if response.status_code >= 400:
            try:
                error = response.json()
                message = (
                    error.get("message")
                    or error.get("msg")
                    or error.get("error_description")
                    or str(error)
                )
            except ValueError:
                message = response.text

            raise HTTPException(
                status_code=response.status_code,
                detail=message
            )

        if response.status_code == 204 or not response.content:
            return None

        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar ao Supabase."
        )