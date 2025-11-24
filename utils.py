import os
import hashlib
import base64
import hmac

def hash_password(password: str, salt: bytes | None = None, iterations: int = 200_000) -> str:
    if salt is None:
        salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return base64.b64encode(salt + dk).decode("utf-8")

def verify_password(password: str, stored: str, iterations: int = 200_000) -> bool:
    b = base64.b64decode(stored.encode("utf-8"))
    salt = b[:16]
    dk = b[16:]
    new = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return hmac.compare_digest(dk, new)