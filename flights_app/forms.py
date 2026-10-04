from django import forms
from .models import Flight, Passenger
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'duration']
    widgets ={
        'origin': forms.TextInput(attrs={'class': 'form-control'}),
        'destination': forms.TextInput(attrs={'class': 'form-control'}),
        'duration': forms.NumberInput(attrs={'class': 'form-control', 'min': 10}),
    }
class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first', 'last', 'flights', 'image']
    widgets = {
        'first': forms.TextInput(attrs={'class': 'form-control'}),
        'last': forms.TextInput(attrs={'class': 'form-control'}),
        'flights': forms.SelectMultiple(attrs={'class': 'form-control'}),
        'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
    }
