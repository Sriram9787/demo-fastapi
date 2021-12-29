from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, VARCHAR
from .database import Base
from sqlalchemy import Integer,Column,BIGINT,CHAR,TEXT

#user
class User(Base):
    __tablename__ = "user"
    id = Column(BIGINT,primary_key=True,nullable=False)
    username = Column(VARCHAR(length=20),nullable=False,unique=True)
    email = Column(CHAR(length=30),nullable=False,unique=True)
    password = Column(CHAR(length=60),nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True))
    created_at = Column(TIMESTAMP(timezone=True),server_default=text("now()"))



#post
class Post(Base):
    __tablename__ = "post"
    id = Column(BIGINT,primary_key=True,nullable=False)
    title = Column(CHAR(length=150),nullable=False)
    content = Column(TEXT)
    user_id = Column(BIGINT,ForeignKey("user.id",ondelete="CASCADE"),nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True))
    created_at = Column(TIMESTAMP(timezone=True),server_default=text("now()"))