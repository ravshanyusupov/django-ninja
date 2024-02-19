from ninja import Schema
from ninja import ModelSchema
from datetime import date
from todo.models import Todo


class responseSchema(ModelSchema):
    status: int = 201
    message: str = 'created'
    timestamp: date = date.today()

    class Meta:
        model = Todo
        fields = ["id", "title", "deadline", "body", "is_completed", "state"]


class createSchema(Schema):
    title: str
    deadline: date = date.today()
    body: str
    is_completed: bool = False


