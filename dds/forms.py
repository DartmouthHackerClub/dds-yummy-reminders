from django import forms
from dds.models import Subscription

class SubscribeForm(forms.Form):
    email = forms.EmailField()
    food = forms.CharField()

class DDSForm(forms.Form):
    food = forms.CharField()
