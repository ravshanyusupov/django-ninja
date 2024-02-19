from ninja import Schema
import datetime


class changeSchema(Schema):
    status: int = 203
    message: str = 'modified'
    timestamp: datetime.date = datetime.datetime.now()