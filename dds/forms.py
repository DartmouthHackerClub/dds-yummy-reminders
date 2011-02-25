from django import forms
from dds.models import Subscription

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email', 'food',)

class DDSForm(forms.Form):
    food = forms.CharField()
