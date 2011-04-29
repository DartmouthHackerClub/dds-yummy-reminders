#!/usr/bin/env python

import dds_scrape
from django.core.mail import send_mail
from django.conf import settings
from dds.models import Subscription

FROM_EMAIL = 'hacktown-noreply@hacktown.cs.dartmouth.edu'

print 'OKKKAAYYYYY'
    
prev_sub = None
body = []
subject = []

def mail(subj, bod, to):
    print 'sending mail to', to
    body.append("---\nThis is a service of Hacker Club.\nTo cancel all notifications, go here:")
    body.append(prev_sub.unsubscribe_all_link())
    full_subject = "[DDS TODAY]: "+", ".join(subj)
    full_body = '\n'.join(bod)
    try:
        send_mail(full_subject, full_body, FROM_EMAIL, [to])
    except:
        print 'error sending mail to', prev_sub.email
        return
    print 'sent mail to', prev_sub.email

# mimics nested for loops to minimize queries
for sub in Subscription.objects.all().order_by('email'):
    print 'reached', sub.email

    if prev_sub != None:
        if sub.email != prev_sub.email:
            print 'We\'re done processing matches for', prev_sub.email
            if body:
                mail(subject, body, prev_sub.email)
            body = []
            subject = []
        elif sub.food == prev_sub.food:
            # duplicate
            continue

    items = dds_scrape.isThere(sub.food.encode('utf-8'))
    
    if items:
        subject.append(sub.food.lower())
        body.append("%s!" % (sub.food.upper()))
        print 'items:',items
        foods = '\n'.join(["%s @ %s [%s]" %  (food, loc, cat.replace('\n', '-')) for food,cat,loc in items])
        print 'matched', foods
        body.append(foods.decode('utf-8'))
        body.append("(unsubscribe from this item: %s)\n" % (sub.unsubscribe_link(),))

    prev_sub = sub

print 'exited loop'
# last mail
if body:
    mail(subject, body, prev_sub.email)
