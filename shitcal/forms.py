from django.forms import ModelForm

from shitcal.models import Shit

class ShitForm(ModelForm):
    talk = forms.BooleanField(required=False)
    date = forms.DateField(required=True)
    description = forms.CharField(required=False)
