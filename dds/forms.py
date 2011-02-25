from django import forms

class DDSForm(forms.Form):
    food = forms.CharField()
