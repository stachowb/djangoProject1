from django import forms
from .models import Company


class CompanyCreateForm(forms.ModelForm):
    """
    Company creation form
    """
    class Meta:
        model = Company
        fields = ['name']