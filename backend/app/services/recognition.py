
from app.schemas.translations import SignLandmarksRequest


def recognize_landmarks(dados: SignLandmarksRequest):
    """
    Recebe uma sequência de landmarks identificados pela câmera.

    Nesta primeira etapa, valida e prepara os dados.
    O classificador será conectado quando tivermos
    um modelo treinado com exemplos reais de Libras.
    """

    quantidade_frames = len(dados.frames)

    frames_com_mao_esquerda = sum(
        1 for frame in dados.frames
        if frame.left_hand is not None
    )

    frames_com_mao_direita = sum(
        1 for frame in dados.frames
        if frame.right_hand is not None
    )

    return {
        "status": "model_not_trained",
        "message": (
            "Os movimentos foram recebidos e validados. "
            "O modelo de reconhecimento ainda está em preparação."
        ),
        "frames_received": quantidade_frames,
        "left_hand_frames": frames_com_mao_esquerda,
        "right_hand_frames": frames_com_mao_direita,
        "fps": dados.fps,
        "recognized_sign": None,
        "confidence": None
    }
