from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    
class Subscription(models.Model):
    profile = models.ForeignKey(Profile)
    food = models.CharField()
