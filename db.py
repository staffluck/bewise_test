from config import Settings

db_url = Settings.DB_DSN

TORTOISE_ORM = {
    "connections": {"default": db_url},
    "apps": {
        "contact": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
