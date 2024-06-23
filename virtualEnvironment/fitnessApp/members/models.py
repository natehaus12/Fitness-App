from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
  firstname = models.CharField(max_length=255)
 


class Food(models.Model):
  food_name = models.CharField(max_length=255)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.TextField()
    weight = models.TextField()
    goal = models.TextField()
    
    def __str__(self):
        return self.user.username
