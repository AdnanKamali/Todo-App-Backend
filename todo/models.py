from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class DurationModel(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

class TodoModel(models.Model):
    title = models.CharField(max_length=255)
    duration = models.ForeignKey(DurationModel, on_delete=models.CASCADE)
    description = models.TextField()

class UserTodo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    todos = models.ManyToManyField(TodoModel)