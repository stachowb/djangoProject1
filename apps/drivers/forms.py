from django import forms
from .models import Driver


class DriverCreationForm(forms.ModelForm):
    """
    Driver creation form
    """
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'company', 'vehicle']