from django.db import models
from datetime import datetime


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]


class Todo(TimeStampedModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    deadline = models.DateTimeField(null=False)
    body = models.TextField()
    is_completed = models.BooleanField(default=False)
    state = models.IntegerField(default=1)

    def __repr__(self):
        return str(self.title)
