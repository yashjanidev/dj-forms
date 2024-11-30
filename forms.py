from django import forms
from .models import EventInfo

class EventFormdata(forms.ModelForm):
    class Meta:
        model = EventInfo
        fields = '__all__'
