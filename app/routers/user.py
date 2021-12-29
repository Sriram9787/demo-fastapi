from fastapi import APIRouter,HTTPException,status
from fastapi.param_functions import Depends
from ..schemas import SendUser,LoginUser
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..utils import hash_password,verify_password
from ..oauth2 import create_token,get_current_user


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

#register user
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(user: SendUser,db: Session = Depends(get_db)):
    password = user.password
    user.password = hash_password(password)
    user = User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


#login user
@router.post('/login')
def login_user(user: LoginUser,db: Session = Depends(get_db)):
    current_user = db.query(User).filter((User.username == user.username) | (User.email == user.username)  ).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"NO user with {user.username} found")
    
    if not verify_password(user.password,current_user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"wrong password")
    
    access_token = create_token(data = {"id":current_user.id})
    return access_token


