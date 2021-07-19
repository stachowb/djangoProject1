from django import forms
from .models import Shift


class ShiftCreationForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['driver', 'reg_number', 'clock_in', 'clock_out', 'distance']