from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(passowrd: str,hashed_password: str):
    return pwd_context.verify(passowrd,hashed_password)