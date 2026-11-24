from fastapi import APIRouter, Depends

from app.security import get_current_user
from app.services.supabase import supabase_request

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
async def get_dashboard(user=Depends(get_current_user)):
    headers_token = user["token"]

    traducoes = await supabase_request(
        method="GET",
        path="/rest/v1/traducoes",
        token=headers_token,
        params={
            "select": "id",
            "usuario_id": f"eq.{user['id']}",
            "limit": 1000
        }
    )

    progresso = await supabase_request(
        method="GET",
        path="/rest/v1/progresso_aprendizado",
        token=headers_token,
        params={
            "select": "id",
            "usuario_id": f"eq.{user['id']}",
            "concluida": "eq.true",
            "limit": 1000
        }
    )

    licoes = await supabase_request(
        method="GET",
        path="/rest/v1/licoes",
        params={
            "select": "id",
            "limit": 1000
        }
    )

    return {
        "success": True,
        "dashboard": {
            "total_traducoes": len(traducoes),
            "licoes_concluidas": len(progresso),
            "total_licoes": len(licoes)
        }
    }