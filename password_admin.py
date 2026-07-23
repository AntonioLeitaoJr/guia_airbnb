import base64
import hashlib
import hmac
import json
import os
import secrets
from pathlib import Path

from config import get_config

ARQUIVO_SENHA_ADMIN = Path(".admin_password.json")
ITERACOES_PBKDF2 = 260_000
TAMANHO_SALT = 16


def _gerar_hash(senha: str, salt: bytes | None = None) -> dict[str, str | int]:
    salt = salt or secrets.token_bytes(TAMANHO_SALT)
    hash_senha = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt,
        ITERACOES_PBKDF2,
    )
    return {
        "algoritmo": "pbkdf2_sha256",
        "iteracoes": ITERACOES_PBKDF2,
        "salt": base64.b64encode(salt).decode("ascii"),
        "hash": base64.b64encode(hash_senha).decode("ascii"),
    }


def _carregar_registro() -> dict[str, str | int] | None:
    if not ARQUIVO_SENHA_ADMIN.exists():
        return None

    try:
        with ARQUIVO_SENHA_ADMIN.open("r", encoding="utf-8") as arquivo:
            registro = json.load(arquivo)
    except (OSError, json.JSONDecodeError):
        return None

    campos_obrigatorios = {"algoritmo", "iteracoes", "salt", "hash"}
    if not campos_obrigatorios.issubset(registro):
        return None
    return registro


def senha_admin_configurada_localmente() -> bool:
    return _carregar_registro() is not None


def verificar_senha_admin(senha: str) -> bool:
    registro = _carregar_registro()
    if registro:
        salt = base64.b64decode(str(registro["salt"]))
        hash_armazenado = base64.b64decode(str(registro["hash"]))
        hash_informado = hashlib.pbkdf2_hmac(
            "sha256",
            senha.encode("utf-8"),
            salt,
            int(registro["iteracoes"]),
        )
        return hmac.compare_digest(hash_informado, hash_armazenado)

    senha_admin = get_config("ADMIN_PASSWORD", "admin123")
    return hmac.compare_digest(senha, senha_admin or "")


def atualizar_senha_admin(nova_senha: str) -> None:
    registro = _gerar_hash(nova_senha)
    arquivo_temporario = ARQUIVO_SENHA_ADMIN.with_suffix(".tmp")

    with arquivo_temporario.open("w", encoding="utf-8") as arquivo:
        json.dump(registro, arquivo, ensure_ascii=False, indent=2)
        arquivo.write("\n")

    os.replace(arquivo_temporario, ARQUIVO_SENHA_ADMIN)
