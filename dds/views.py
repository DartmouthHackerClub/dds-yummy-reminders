import string
import urllib2
from random import choice

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

from dds.forms import DDSForm
from dds.forms import SubscribeForm
from dds.models import Subscription
from dds.transforms import AUTOCORRECT

def subscribe(request):
    if request.POST:
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            food = form.cleaned_data['food'].split(',')
            text = ["The following subscriptions were added for %s:" % (email,)]
            last_sub = None
            for item in food:  # give each item (comma-delimited) a separate subscription
                item = item.strip().lower()
                if item: # ignore empty strings (or purely whitespace strings)
                    s = Subscription()
                    s.food = AUTOCORRECT[item] if item in AUTOCORRECT else item
                    s.email = email
                    s.tag = ''.join([choice(string.letters + string.digits) for i in range(10)])

#                    if len(Subscription.objects.filter(food=s.food, email=email)) > 0:
#                        continue

                    s.save()
                    text.append('%s (cancel here: %s)' % (s.food.lower(), s.unsubscribe_link())) 
                    last_sub = s
           
            if last_sub != None: 
                text.append('\n cancel all subscriptions: %s' % (last_sub.unsubscribe_all_link()))
                send_mail('subscription added', '\n'.join(text), 'hacktown-noreply@hacktown.cs.dartmouth.edu', [email], fail_silently=False)
                return render_to_response('dds/subscriptions.html', {
                    'form':form,
                    'comment':'thanks, your subscription was entered',
                })
        
        # else if form's invalid or last_sub = None    
        return render_to_response('dds/subscriptions.html', {
            'form':form,
            'comment':'invalid entry - maybe you already subscribed to this stuff?',
        })
    else:
        form = SubscribeForm()

    return render_to_response('dds/subscriptions.html', {
        'form':form,
    })

def unsubscribe(request, email, tag):
    try:
        subscription = Subscription.objects.get(email=email, tag=tag) 
        text = 'Removed subscription: %s' % (subscription.food.lower())
        subscription.delete()
        return HttpResponse(text)
    except ObjectDoesNotExist:
        return HttpResponse('Removal failed - contact hacker club')

def unsubscribe_all(request, email, tag):
    try:
        # Verify that at least one tag is accurate, then delete the rest
        s = Subscription.objects.get(email=email, tag=tag)
        subscriptions = Subscription.objects.filter(email=email)
        for sub in subscriptions:
            sub.delete()
        return HttpResponse('Removed all your subscriptions successfully')
    except ObjectDoesNotExist:
        return HttpResponse('Removal failed - contact hacker club')
    

def generaltso(request):
    html = urllib2.urlopen('http://www.dartmouth.edu/dining/').read()
    if html.lower().find('general tso') > -1:
        return HttpResponse('<center><h1>YES</h1></center>')
    return HttpResponse('<center><h1>NO</h1></center>')

def lookfor(request):
    if request.method == 'POST':
        form = DDSForm(request.POST)
        if form.is_valid():
            html = urllib2.urlopen('http://www.dartmouth.edu/dining/').read().decode('utf-8')
            if html.lower().find(form.cleaned_data['food']) > -1:
                return HttpResponse('<center><h1>YES</h1></center>')
            return HttpResponse('<center><h1>NO</h1></center>')
    else:
        form = DDSForm()

    return render_to_response('dds/lookfor.html', {
        'form':form,
    })
