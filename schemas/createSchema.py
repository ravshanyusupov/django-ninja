
from typing import Optional

from ninja import Schema
from ninja import ModelSchema
from datetime import date, datetime
from todo.models import Todo


class responseSchema(ModelSchema):
    status: int = 201
    message: str = 'created'
    timestamp: date

    class Meta:
        model = Todo
        fields = ["id", "deadline", "is_completed", "state"]


class createSchema(Schema):
    title: str
    deadline: date = datetime.now()
    body: str
    is_completed: bool = False


