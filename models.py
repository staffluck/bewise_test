from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class BaseModel(models.Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True


class Trivia(BaseModel):
    question_id = fields.IntField()
    question = fields.TextField()
    answer = fields.CharField(max_length=155)
    created_at = fields.DatetimeField()

    class Meta:
        table = "trivias"


TriviaSchema = pydantic_model_creator(Trivia, name="Trivia")
