from django.db import models

class Subscription(models.Model):
    email = models.EmailField()
    food = models.CharField()
