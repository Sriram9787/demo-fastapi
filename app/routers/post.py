from fastapi import APIRouter,status,HTTPException
from fastapi.param_functions import Depends
from ..schemas import SendPost
from ..database import get_db
from sqlalchemy.orm import Session
from ..models import Post, User
from ..oauth2 import get_current_user

router = APIRouter(
    prefix='/post',
    tags=['POST']
)



@router.get('/')
def get_post(db: Session = Depends(get_db),current_user: int = Depends(get_current_user)):
    post = db.query(Post).filter(Post.user_id == current_user.id).all()
    return post

@router.get('/all')
def get_all_post(db: Session = Depends(),current_user: int = Depends(get_current_user)):
   pass

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_post(post: SendPost,db: Session = Depends(get_db),current_user: int = Depends(get_current_user)):
    post = Post(user_id = current_user.id,**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
    #pm.response.json().access_token
    

@router.post('/update')
def update_post():
    pass

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db),current_user: int = Depends(get_current_user)):
    post_query = db.query(Post).filter_by(Post.id == id)
    post = post_query.first()
    post_query.delete(synchronize_session=False)
    db.commit()
