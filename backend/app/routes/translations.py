
from fastapi import APIRouter, Depends, HTTPException, Query

from app.security import get_current_user
from app.schemas.translations import (
    TranslationCreate,
    TextToSignRequest,
    SignToTextRequest,
    SignLandmarksRequest
)
from app.services.supabase import supabase_request
from app.services.libras import text_to_sign, sign_to_text
from app.services.recognition import recognize_landmarks

router = APIRouter(
    prefix="/api/translations",
    tags=["Traduções"]
)


@router.post("/text-to-sign")
async def translate_text_to_sign(
    dados: TextToSignRequest,
    user=Depends(get_current_user)
):
    resultado = text_to_sign(dados.texto)

    return {
        "success": True,
        "translation": resultado
    }


# Reconhecimento de Libras usando os pontos identificados pela câmera
@router.post("/sign-to-text/landmarks")
async def translate_landmarks_to_text(
    dados: SignLandmarksRequest,
    user=Depends(get_current_user)
):
    resultado = recognize_landmarks(dados)

    return {
        "success": True,
        "recognition": resultado
    }


# Rota antiga mantida para compatibilidade
@router.post("/sign-to-text")
async def translate_sign_to_text(
    dados: SignToTextRequest,
    user=Depends(get_current_user)
):
    resultado = sign_to_text()

    raise HTTPException(
        status_code=501,
        detail=resultado["message"]
    )


@router.get("/")
async def list_translations(
    limite: int = Query(default=20, ge=1, le=100),
    user=Depends(get_current_user)
):
    dados = await supabase_request(
        method="GET",
        path="/rest/v1/traducoes",
        token=user["token"],
        params={
            "select": "*",
            "usuario_id": f"eq.{user['id']}",
            "order": "criado_em.desc",
            "limit": limite
        }
    )

    return {
        "success": True,
        "total": len(dados),
        "translations": dados
    }


@router.post("/", status_code=201)
async def save_translation(
    dados: TranslationCreate,
    user=Depends(get_current_user)
):
    resultado = await supabase_request(
        method="POST",
        path="/rest/v1/traducoes",
        token=user["token"],
        json={
            "usuario_id": user["id"],
            "tipo": dados.tipo,
            "texto_entrada": dados.texto_entrada,
            "texto_saida": dados.texto_saida
        },
        prefer="return=representation"
    )

    return {
        "success": True,
        "message": "Tradução salva no histórico.",
        "translation": resultado[0] if resultado else None
    }


@router.delete("/{translation_id}")
async def delete_translation(
    translation_id: str,
    user=Depends(get_current_user)
):
    await supabase_request(
        method="DELETE",
        path="/rest/v1/traducoes",
        token=user["token"],
        params={
            "id": f"eq.{translation_id}",
            "usuario_id": f"eq.{user['id']}"
        }
    )

    return {
        "success": True,
        "message": "Solicitação de exclusão concluída."
    }


@router.delete("/")
async def clear_translations(
    user=Depends(get_current_user)
):
    await supabase_request(
        method="DELETE",
        path="/rest/v1/traducoes",
        token=user["token"],
        params={
            "usuario_id": f"eq.{user['id']}"
        }
    )

    return {
        "success": True,
        "message": "Histórico limpo."
    }
