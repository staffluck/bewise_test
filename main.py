from fastapi import FastAPI
import uvicorn


def get_app():
    _app = FastAPI(
        title="TechTask",
        debug=True,
    )

    return _app


app = get_app()
