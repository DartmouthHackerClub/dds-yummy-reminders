from random import choice
import string
from django.http import HttpResponse
from django.shortcuts import render_to_response
from dds.forms import DDSForm
from dds.forms import SubscribeForm
from dds.models import Subscription
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
import urllib2

def subscribe(request):
    if request.POST:
        form = SubscribeForm(request.POST)
        if form.is_valid():
            s = Subscription()
            s.food = form.cleaned_data['food']
            s.email = form.cleaned_data['email']
            s.tag = ''.join([choice(string.letters + string.digits) for i in range(6)])
            s.save()

            text = 'Your subscription to %s was added.\nYou can unsubscribe from this food item at: %s\n or cancel all your subscriptions at: %s' % (s.food, s.unsubscribe_link(), s.unsubscribe_all_link())
            send_mail('subscription added', text, 'hacktown-noreply@hacktown.cs.dartmouth.edu', [s.email], fail_silently=False)
            return render_to_response('dds/subscriptions.html', {
                'form':form,
                'comment':'thanks, your subscription was entered',
            })
        else:
            return render_to_response('dds/subscriptions.html', {
                'form':form,
                'comment':'invalid entry',
            })
    else:
        form = SubscribeForm()

    return render_to_response('dds/subscriptions.html', {
        'form':form,
    })

def unsubscribe(request, email, tag):
    try:
        subscription = Subscription.objects.get(email=email, tag=tag)
        subscription.delete()
        return HttpResponse('Removed successfully')
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
