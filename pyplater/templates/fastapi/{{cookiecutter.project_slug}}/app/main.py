from fastapi import FastAPI
import db.model as models
from db.database import engine
from routers import auth, posts
import uvicorn
from config import settings

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, tags=['auth'])
app.include_router(posts.router, tags=['posts'])

if __name__ == '__main__':
    uvicorn.run(app, host=settings.host, port=settings.port)