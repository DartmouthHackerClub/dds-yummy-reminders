#!/usr/bin/env python

from james.scrape import isThere
from django.core.mail import send_mail
from dds.models import Subscription

FROM_EMAIL = 'hacktown-noreply@hacktown.cs.dartmouth.edu'
    
prev_sub = None

# Subscriptions: [email, food]
# mimics nested for loops to minimize queries
for sub in Subscription.objects.all().order_by('email'):
    if prev_sub != None and sub.email != prev_sub.email:
        if body:
            send_mail("[DDS TODAY]: "+", ".join(subject), '\n'.join(body), FROM_EMAIL, [sub.email])
        body = []
        subject = []
        prev_sub = sub
            

    items = isThere(sub.food)
    
    if items:
        # sorry this is a little hacky/sloppy/whatever
        body.append("%s! YOUR FAVORITE!" % (sub.food.upper(),))
        body.extend(["%s @ %s [%s]" %  (food, loc, cat) for food,cat,loc in items])
        body.append("") #add a filler line to seperate query terms
        subject.append(sub.food.lower())
        body.append("---\nThis is a service of Hacker Club. To unsubscribe, go here:")
        body.append(sub.unsubscribe_link())

if body:
    send_mail("[DDS TODAY]: "+", ".join(subject), '\n'.join(body), FROM_EMAIL, [prev_sub.email])
