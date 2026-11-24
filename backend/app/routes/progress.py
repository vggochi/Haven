from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from app.security import get_current_user
from app.services.supabase import supabase_request

router = APIRouter(
    prefix="/api/progress",
    tags=["Progresso"]
)


class ProgressUpdate(BaseModel):
    concluida: bool = True
    pontuacao: int | None = Field(
        default=None,
        ge=0,
        le=100
    )


@router.get("/")
async def get_progress(user=Depends(get_current_user)):
    dados = await supabase_request(
        method="GET",
        path="/rest/v1/progresso_aprendizado",
        token=user["token"],
        params={
            "select": "*",
            "usuario_id": f"eq.{user['id']}"
        }
    )

    return {
        "success": True,
        "total": len(dados),
        "progress": dados
    }


@router.put("/{lesson_id}")
async def update_progress(
    lesson_id: str,
    dados: ProgressUpdate,
    user=Depends(get_current_user)
):
    atualizacao = {
        "usuario_id": user["id"],
        "licao_id": lesson_id,
        "concluida": dados.concluida
    }

    if dados.pontuacao is not None:
        atualizacao["pontuacao"] = dados.pontuacao

    resultado = await supabase_request(
        method="POST",
        path="/rest/v1/progresso_aprendizado",
        token=user["token"],
        params={
            "on_conflict": "usuario_id,licao_id"
        },
        json=atualizacao,
        prefer="resolution=merge-duplicates,return=representation"
    )

    return {
        "success": True,
        "message": "Progresso atualizado.",
        "progress": resultado[0] if resultado else None
    }