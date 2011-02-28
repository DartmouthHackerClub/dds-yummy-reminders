#!/usr/bin/env python

import dds_scrape
from django.core.mail import send_mail
from django.conf import settings
from dds.models import Subscription

FROM_EMAIL = 'hacktown-noreply@hacktown.cs.dartmouth.edu'
    
prev_sub = None
body = []
subject = []

def mail(subj, bod, to):
    body.append("---\nThis is a service of Hacker Club. To unsubscribe from this foot item, go here:")
    body.append(sub.unsubscribe_link())
    body.append("To unsubscribe from all notifications:")
    body.append(sub.unsubscribe_all_link())
    send_mail("[DDS TODAY]: "+", ".join(subj), '\n'.join(bod), FROM_EMAIL, [to])
    print 'sent mail to', prev_sub.email

# Subscriptions: [email, food]
# mimics nested for loops to minimize queries
for sub in Subscription.objects.all().order_by('email'):
    if prev_sub != None and sub.email != prev_sub.email:
        if body:
            mail(subject, body, prev_sub.email)
        body = []
        subject = []

    items = dds_scrape.isThere(sub.food.encode('utf-8'))
    
    if items:
        # sorry this is a little hacky/sloppy/whatever
        subject.append(sub.food.lower())
        body.append("%s! YOUR FAVORITE!" % (sub.food.upper(),))
        body.extend(["%s @ %s [%s]" %  (food, loc, cat) for food,cat,loc in items])
        body.append("") #filler line to seperate query terms

    prev_sub = sub

# last mail
if body:
    mail(subject, body, prev_sub.email)
