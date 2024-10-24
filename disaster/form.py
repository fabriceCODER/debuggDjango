from django import forms
from .models import Disaster

class DisasterForm(forms.ModelForm):
    class Meta:
        model = Disaster
        fields = ['name', 'description', 'location', 'date']
