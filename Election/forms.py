from django import forms
from .models import *

class PUForm(forms.ModelForm):
    class Meta:
        model = PollingUnit
        fields = ['lga_id','uniquewardid','polling_unit_id']
        labels = {'lga_id': 'Lga Name','uniquewardid':'Ward Name','polling_unit_id':'Polling Unit Name'}

class Lgaform(forms.ModelForm):
    class Meta:
        model = PollingUnit
        fields = ['lga_id']
        labels = {'lga_id': 'Lga Name'}
    

class NewPUForm(forms.ModelForm):
    class Meta:
        model = New_Polling_Unit
        fields = "__all__"


        