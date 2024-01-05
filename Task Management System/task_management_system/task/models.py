from django.db import models
from django.utils import timezone
from category.models import TaskCategory
# Create your models here.
class TaskModel(models.Model):
    task_title=models.CharField(max_length=100)
    describtion=models.TextField(max_length=300)
    complete=models.BooleanField(default=False)
    category=models.ManyToManyField(TaskCategory)
    task_assigned_date=models.DateTimeField(default=timezone.now)
    def __str__(self):
      return self.task_title