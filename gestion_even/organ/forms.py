from django import forms
from betterforms.multiform import MultiModelForm

from events.models import Event, EventImage, EventAgenda


class EventForm(forms.ModelForm):

    status_choices = [
        ('disabled', 'Disabled'),
    ]
    status = forms.ChoiceField(choices=status_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Event
        fields = ['category', 'name',  'description', 'job_category', 'scheduled_status', 'venue', 'start_date', 'end_date', 'location', 'maximum_attende','price', 'status']
        widgets = {
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class EventImageForm(forms.ModelForm):


    class Meta:
        model = EventImage
        fields = ['image']



class EventAgendaForm(forms.ModelForm):


    class Meta:
        model = EventAgenda
        fields = [ 'speaker_name', 'start_time', 'end_time']

        widgets = {
            'start_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }


class EventCreateMultiForm(MultiModelForm):
    form_classes = {
        'event': EventForm,
        'event_image': EventImageForm,
        'event_agenda': EventAgendaForm,
    }


class EventUpdateForm(forms.ModelForm):
    status_choices = [
        ('disabled', 'Disabled'),
    ]

    status = forms.ChoiceField(choices=status_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Event
        fields = ['category', 'name', 'description', 'scheduled_status', 'venue', 'start_date', 'end_date', 'location', 'maximum_attende', 'price', 'status']
