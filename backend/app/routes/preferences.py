from fastapi import APIRouter, Depends, HTTPException

from app.security import get_current_user
from app.schemas.profile import PreferencesUpdate
from app.services.supabase import supabase_request

router = APIRouter(
    prefix="/api/preferences",
    tags=["Preferências"]
)


@router.get("/")
async def get_preferences(user=Depends(get_current_user)):
    dados = await supabase_request(
        method="GET",
        path="/rest/v1/perfis",
        token=user["token"],
        params={
            "select": "idioma_interface,tamanho_texto,notificacoes_ativas",
            "id": f"eq.{user['id']}"
        }
    )

    if not dados:
        raise HTTPException(
            status_code=404,
            detail="Preferências não encontradas."
        )

    return {
        "success": True,
        "preferences": dados[0]
    }


@router.patch("/")
async def update_preferences(
    dados: PreferencesUpdate,
    user=Depends(get_current_user)
):
    atualizacoes = dados.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    if not atualizacoes:
        raise HTTPException(
            status_code=400,
            detail="Informe pelo menos uma preferência."
        )

    resultado = await supabase_request(
        method="PATCH",
        path="/rest/v1/perfis",
        token=user["token"],
        params={
            "id": f"eq.{user['id']}",
            "select": "idioma_interface,tamanho_texto,notificacoes_ativas"
        },
        json=atualizacoes,
        prefer="return=representation"
    )

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Perfil não encontrado."
        )

    return {
        "success": True,
        "message": "Preferências atualizadas.",
        "preferences": resultado[0]
    }