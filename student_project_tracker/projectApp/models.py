from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class userModel(AbstractUser):
    student_name=models.CharField(max_length=100,null=True)
    student_id=models.TextField(null=True)





class projectModel(models.Model):
    project_name=models.CharField(max_length=100,null=True)
    project_description=models.TextField(null=True)
    deadline=models.CharField(max_length=100,null=True)
    project_status=models.CharField(max_length=100,null=True,choices=[
        ('NotStarted','NotStarted'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
    ])
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)
    created_by=models.ForeignKey(userModel,on_delete=models.CASCADE,null=True)

