

from ninja import Schema


class UserIn(Schema):
    status: int = 201
    message: str = 'created'


response = UserIn




def handler(request):
    return "delete"