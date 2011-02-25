from django.db import models

class Subscription(models.Model):
    email = models.EmailField()
    food = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s subscribed to %s' % (email, food)
