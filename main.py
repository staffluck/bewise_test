from fastapi import FastAPI
from db import init_db


def get_app():
    _app = FastAPI(
        title="TechTask",
        debug=True,
    )

    return _app


app = get_app()


@app.get("/")
async def test():
    return "someting"


@app.on_event("startup")
async def startup_event():
    init_db(app)
