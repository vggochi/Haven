
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import FRONTEND_URL

from app.routes import (
    auth,
    profile,
    preferences,
    translations,
    lessons,
    progress,
    dashboard
)

app = FastAPI(
    title="HAVEN API",
    description=(
        "API da plataforma HAVEN — "
        "Comunicação e acessibilidade em Libras."
    ),
    version="1.0.0"
)

# Configuração de acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        FRONTEND_URL,
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def home():
    return {
        "success": True,
        "name": "HAVEN API",
        "message": "API funcionando corretamente.",
        "version": "1.0.0"
    }


@app.get("/api/health")
async def health():
    return {
        "success": True,
        "status": "online",
        "service": "HAVEN API"
    }


# Registro das rotas
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(preferences.router)
app.include_router(translations.router)
app.include_router(lessons.router)
app.include_router(progress.router)
app.include_router(dashboard.router)
