from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

from config import settings


db_url = settings.DB_DSN

TORTOISE_ORM = {
    "connections": {"default": str(db_url)},
    "apps": {
        "trivia": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=str(db_url),
        modules={"models": ["models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
