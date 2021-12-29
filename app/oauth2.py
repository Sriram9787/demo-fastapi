from fastapi.param_functions import Depends
from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from app.models import User
from .schemas import TokenData
from sqlalchemy.orm import Session
from .database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return {"access_token": encoded_jwt, "token_type": "bearer"}

def verify_token(token,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        payload_id: str = payload.get("id")
        if payload_id is None:
            raise credentials_exception
        token_data = TokenData(user_id = payload_id)
    except JWTError:
        raise credentials_exception

    return token_data

def get_current_user(token: str=Depends(oauth2_scheme),db: Session = Depends(get_db)):
      credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
      token = verify_token(token,credentials_exception)
      user = db.query(User).filter(User.id == token.user_id).first()
      return user
    



