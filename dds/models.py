from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    email = models.EmailField()
    food = models.CharField()
    activated = models.BooleanField()
