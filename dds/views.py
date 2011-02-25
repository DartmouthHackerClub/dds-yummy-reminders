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
            s.save()

            text = 'Your subscription to %s was added.' % (s.food)
            send_mail('subscription added', text, 'hacktown@dartmouth.edu', [s.food], fail_silently=False)
            return HttpResponse('thanks')
        else:
            return HttpResponse('invalid')
    else:
        form = SubscribeForm()

    return render_to_response('dds/subscriptions.html', {
        'form':form,
    })

def unsubscribe(request, email, id):
    try:
        subscription = Subscription.objects.get(pk=id, email=email)
        subscription.delete()
        return HttpResponse('Removed')
    except ObjectDoesNotExist:
        return HttpResponse('Removal failed')

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
