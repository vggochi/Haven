from pydantic import BaseModel, Field, EmailStr


class ProfileUpdate(BaseModel):
    nome_exibicao: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    email: EmailStr | None = None

    biografia: str | None = Field(
        default=None,
        max_length=500
    )

    avatar_url: str | None = None


class PreferencesUpdate(BaseModel):
    idioma_interface: str | None = Field(
        default=None,
        max_length=10
    )

    tamanho_texto: str | None = Field(
        default=None,
        max_length=20
    )

    notificacoes_ativas: bool | None = None