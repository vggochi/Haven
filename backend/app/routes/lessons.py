from fastapi import APIRouter, HTTPException

from app.services.supabase import supabase_request

router = APIRouter(
    prefix="/api/lessons",
    tags=["Aprendizado"]
)


@router.get("/")
async def list_lessons():
    dados = await supabase_request(
        method="GET",
        path="/rest/v1/licoes",
        params={
            "select": "*",
            "order": "id.asc"
        }
    )

    return {
        "success": True,
        "total": len(dados),
        "lessons": dados
    }


@router.get("/{lesson_id}")
async def get_lesson(lesson_id: str):
    dados = await supabase_request(
        method="GET",
        path="/rest/v1/licoes",
        params={
            "select": "*",
            "id": f"eq.{lesson_id}"
        }
    )

    if not dados:
        raise HTTPException(
            status_code=404,
            detail="Lição não encontrada."
        )

    return {
        "success": True,
        "lesson": dados[0]
    }