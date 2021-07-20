import django_filters
from .models import Shift


class ShiftFilter(django_filters.FilterSet):

    class Meta:
        model = Shift
        fields = {
            'distance': ['icontains'],
            'clock_in': ['icontains'],
            'clock_out': ['icontains'],
        }
