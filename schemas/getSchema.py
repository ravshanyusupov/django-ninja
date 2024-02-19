from ninja import Schema
import datetime


class getSchema(Schema):
    status: int = 200
    message: str = 'get'
    timestamp: datetime.date = datetime.datetime.now()