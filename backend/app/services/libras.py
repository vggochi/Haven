def text_to_sign(texto: str):
    palavras = texto.strip().split()

    if not palavras:
        return {
            "texto_original": texto,
            "palavras": [],
            "status": "empty"
        }

    return {
        "texto_original": texto,
        "palavras": [
            {
                "palavra": palavra,
                "sinal_disponivel": False,
                "video_url": None,
                "status": "pending_dictionary"
            }
            for palavra in palavras
        ],
        "status": "didactic_preview",
        "notice": (
            "Representação didática palavra por palavra. "
            "Não constitui tradução gramatical para Libras."
        )
    }


def sign_to_text():
    return {
        "status": "not_implemented",
        "message": (
            "O reconhecimento de sinais ainda não está conectado "
            "a um modelo de visão computacional."
        )
    }