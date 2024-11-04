from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    


    def __str__(self):
        return self.todo_title
    