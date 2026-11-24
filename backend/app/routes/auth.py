import os
from urllib.parse import urlencode

from fastapi import APIRouter, Depends

from app.schemas.auth import RegisterRequest, LoginRequest
from app.security import get_current_user
from app.services.supabase import supabase_request


router = APIRouter(
    prefix="/api/auth",
    tags=["Autenticação"]
)


@router.post("/register", status_code=201)
async def register(dados: RegisterRequest):
    # O endereço precisa estar cadastrado em Supabase > Authentication
    # > URL Configuration > Redirect URLs.
    frontend_url = os.getenv(
        "FRONTEND_URL",
        "http://127.0.0.1:5500"
    ).rstrip("/")

    redirect_url = f"{frontend_url}/?confirmed=1"
    signup_path = "/auth/v1/signup?" + urlencode({
        "redirect_to": redirect_url
    })

    resposta = await supabase_request(
        method="POST",
        path=signup_path,
        json={
            "email": dados.email,
            "password": dados.senha,
            "data": {
                "nome_exibicao": dados.nome_exibicao
            }
        }
    )

    return {
        "success": True,
        "message": "Cadastro enviado. Verifique seu e-mail para confirmar sua conta.",
        "user": resposta.get("user"),
        "session": resposta.get("session")
    }


@router.post("/login")
async def login(dados: LoginRequest):
    resposta = await supabase_request(
        method="POST",
        path="/auth/v1/token?grant_type=password",
        json={
            "email": dados.email,
            "password": dados.senha
        }
    )

    return {
        "success": True,
        "message": "Login realizado com sucesso.",
        "access_token": resposta.get("access_token"),
        "refresh_token": resposta.get("refresh_token"),
        "token_type": resposta.get("token_type"),
        "expires_in": resposta.get("expires_in"),
        "user": resposta.get("user")
    }


@router.post("/logout")
async def logout(user=Depends(get_current_user)):
    await supabase_request(
        method="POST",
        path="/auth/v1/logout",
        token=user["token"]
    )

    return {
        "success": True,
        "message": "Sessão encerrada."
    }


@router.get("/me")
async def me(user=Depends(get_current_user)):
    return {
        "success": True,
        "user": user["user"]
    }
