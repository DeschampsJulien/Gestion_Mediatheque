from django import forms

class Ajoutmembre(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

class Ajoutmedia(forms.Form):
    category = forms.CharField(required=False)
    name = forms.CharField(required=False)