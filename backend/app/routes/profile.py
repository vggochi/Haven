from fastapi import APIRouter, Depends, HTTPException

from app.security import get_current_user
from app.schemas.profile import ProfileUpdate
from app.services.supabase import supabase_request

router = APIRouter(
    prefix="/api/profile",
    tags=["Perfil"]
)


@router.get("/")
async def get_profile(user=Depends(get_current_user)):
    dados = await supabase_request(
        method="GET",
        path="/rest/v1/perfis",
        token=user["token"],
        params={
            "select": "*",
            "id": f"eq.{user['id']}"
        }
    )

    if not dados:
        raise HTTPException(
            status_code=404,
            detail="Perfil não encontrado."
        )

    return {
        "success": True,
        "profile": {
            **dados[0],
            "email": user["email"]
        }
    }


@router.patch("/")
async def update_profile(
    dados: ProfileUpdate,
    user=Depends(get_current_user)
):
    atualizacoes = dados.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    novo_email = atualizacoes.pop("email", None)

    if novo_email:
        await supabase_request(
            method="PUT",
            path="/auth/v1/user",
            token=user["token"],
            json={"email": novo_email}
        )

    if atualizacoes:
        resultado = await supabase_request(
            method="PATCH",
            path="/rest/v1/perfis",
            token=user["token"],
            params={
                "id": f"eq.{user['id']}",
                "select": "*"
            },
            json=atualizacoes,
            prefer="return=representation"
        )

        if not resultado:
            raise HTTPException(
                status_code=404,
                detail="Perfil não encontrado ou atualização não permitida."
            )

        perfil = resultado[0]
    else:
        perfil = {}

    return {
        "success": True,
        "message": "Perfil atualizado.",
        "profile": perfil,
        "email_update_requested": bool(novo_email)
    }