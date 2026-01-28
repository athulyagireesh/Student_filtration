from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    cname=models.TextField()

    def __str__(self):
        return self.cname
    
class Students(models.Model):
    name=models.TextField()
    email=models.EmailField()
    age=models.IntegerField()
    phone=models.IntegerField()
    uname=models.ForeignKey(User,on_delete=models.CASCADE)
    cname=models.ForeignKey(Course,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name