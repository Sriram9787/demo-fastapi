from fastapi import FastAPI
from . import models
from .database import ENGINE
from .routers import post,user
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=ENGINE)


app = FastAPI()

origins = [
    "http://localhost:8080",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(user.router)

@app.get('/')
def home():
    return({"data":"hi this is home page"})