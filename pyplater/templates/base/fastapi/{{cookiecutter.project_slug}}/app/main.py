from fastapi import FastAPI
import models
from db import engine
from routers import auth, posts
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, tags=['auth'])
app.include_router(posts.router, tags=['posts'])

if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv('HOST'), port=os.getenv('POST'))