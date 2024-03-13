# task_manager/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.IntegerField(default=None)
    due_date = models.DateField()

    def __str__(self):
        return self.title