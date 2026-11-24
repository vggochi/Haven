
from pydantic import BaseModel, Field, ConfigDict, model_validator


class TranslationCreate(BaseModel):
    tipo: str = Field(
        pattern="^(text_to_sign|sign_to_text)$"
    )
    texto_entrada: str = Field(
        min_length=1,
        max_length=5000
    )
    texto_saida: str = Field(
        min_length=1,
        max_length=10000
    )


class TextToSignRequest(BaseModel):
    texto: str = Field(
        min_length=1,
        max_length=1000
    )


class SignToTextRequest(BaseModel):
    video_url: str | None = None
    observacoes: str | None = Field(
        default=None,
        max_length=500
    )


# Um ponto tridimensional da mão
LandmarkPoint = tuple[float, float, float]


class LandmarkFrame(BaseModel):
    model_config = ConfigDict(allow_inf_nan=False)

    left_hand: list[LandmarkPoint] | None = None
    right_hand: list[LandmarkPoint] | None = None

    @model_validator(mode="after")
    def validate_hands(self):
        if self.left_hand is None and self.right_hand is None:
            raise ValueError(
                "Pelo menos uma mão precisa ser identificada."
            )

        if self.left_hand is not None and len(self.left_hand) != 21:
            raise ValueError(
                "A mão esquerda precisa conter exatamente 21 pontos."
            )

        if self.right_hand is not None and len(self.right_hand) != 21:
            raise ValueError(
                "A mão direita precisa conter exatamente 21 pontos."
            )

        return self


class SignLandmarksRequest(BaseModel):
    frames: list[LandmarkFrame] = Field(
        min_length=1,
        max_length=120
    )

    fps: int = Field(
        default=30,
        ge=1,
        le=60
    )
