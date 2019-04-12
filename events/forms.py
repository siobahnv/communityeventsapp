from django import forms
from django.forms import ModelForm
from .models import Event

# class AddCommunityEvent(forms.Form):
#     event_name = forms.CharField(max_length=200, min_length=1, help_text="Enter event name/title.")
#     start_date = forms.DateField(help_text="Enter start date.")
#     end_date = forms.DateField(help_text="Enter end date.")

class EditCommunityEvent(forms.Form):
    event_name = forms.CharField(max_length=200, min_length=1)
    start_date = forms.DateField()
    end_date = forms.DateField()

class EditEventModelForm(ModelForm):
    class Meta:
        model = Event
        # fields = '__all__'
        exclude = ('tags',)