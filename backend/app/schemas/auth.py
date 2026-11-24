from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    nome_exibicao: str = Field(min_length=2, max_length=100)
    email: EmailStr
    senha: str = Field(min_length=8, max_length=128)


class LoginRequest(BaseModel):
    email: EmailStr
    senha: str = Field(min_length=8, max_length=128)