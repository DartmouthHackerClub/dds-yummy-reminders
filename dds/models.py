from django.db import models

class Subscription(models.Model):
    email = models.EmailField()
    food = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s subscribed to %s' % (self.email, self.food)

    def unsubscribe_link(self):
        return 'http://hacktown.cs.dartmouth.edu/scrape/dds/unsubscribe/%s/%s' % (self.email, self.tag)
