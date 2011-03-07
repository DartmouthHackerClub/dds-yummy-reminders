from django.db import models

class Subscription(models.Model):
    email = models.EmailField()
    food = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s subscribed to %s' % (self.email, self.food)

    def unsubscribe_link(self):
        return 'http://hacktown.cs.dartmouth.edu/dds/app/unsubscribe/%s/%s' % (self.email, self.tag)

    def unsubscribe_all_link(self):
        return 'http://hacktown.cs.dartmouth.edu/dds/app/unsubscribe_all/%s/%s' % (self.email, self.tag)
