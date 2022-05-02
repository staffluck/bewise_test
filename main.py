from fastapi import FastAPI
import aiohttp

from db import init_db
from models import Trivia, TriviaSchema


def get_app():
    _app = FastAPI(
        title="TechTask",
        debug=True,
    )

    return _app


app = get_app()


@app.get("/trivia/")
async def get_trivia(count: int):
    trivia_url = f"https://jservice.io/api/random?count={count}"
    completed = 0
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession() as session:
        while count > completed and count:
            async with session.get(trivia_url, timeout=timeout) as response:
                if response.status == 200:
                    body = await response.json()
                    for item in body:
                        if count >= completed:
                            trivia = Trivia.filter(question_id=item["id"])
                            if not await trivia.exists():
                                trivia = await Trivia.create(
                                    question_id=item["id"],
                                    question=item["question"],
                                    answer=item["answer"],
                                    created_at=item["created_at"],
                                )
                                completed += 1
                        else:
                            break
    last_trivia = await Trivia.all().order_by("-id").first()
    if last_trivia:
        pre_last_trivia = Trivia.filter(id=last_trivia.id - 1)
        if await pre_last_trivia.exists():
            return await TriviaSchema.from_tortoise_orm(await pre_last_trivia.first())
    return {}


@app.on_event("startup")
async def startup_event():
    init_db(app)
