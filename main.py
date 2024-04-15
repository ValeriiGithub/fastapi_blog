from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application(api=FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)):
    app = api
    create_tables()
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"message": "Привет FastAPI🚀"}
