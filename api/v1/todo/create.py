from schemas.createSchema import responseSchema, createSchema
from todo.models import Todo
response = responseSchema


async def handler(request, payload: createSchema):
    data = payload.dict()
    todo = await Todo.objects.acreate(**data)
    print(data)
    # return "create"
