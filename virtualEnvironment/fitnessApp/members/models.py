from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Food(models.Model):
  food_name = models.CharField(max_length=255)

