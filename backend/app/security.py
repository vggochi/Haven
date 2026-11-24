from fastapi import Header, HTTPException

from app.services.supabase import supabase_request


async def get_current_user(
    authorization: str | None = Header(default=None)
):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Autenticação necessária."
        )

    token = authorization.split(" ", 1)[1].strip()

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Token não informado."
        )

    user = await supabase_request(
        method="GET",
        path="/auth/v1/user",
        token=token
    )

    if not user or not user.get("id"):
        raise HTTPException(
            status_code=401,
            detail="Usuário não autenticado."
        )

    return {
        "id": user["id"],
        "email": user.get("email"),
        "user": user,
        "token": token
    }