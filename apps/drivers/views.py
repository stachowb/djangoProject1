from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Driver
from .forms import DriverCreationForm


class DriverCreateView(SuccessMessageMixin, CreateView):
    model = Driver
    form_class = DriverCreationForm
    success_message = "Driver has been added"
    template_name = "drivers/driver-create.html"


class DriverDetailView(DetailView):
    model = Driver
    template_name = "drivers/driver-details.html"
    context_object_name = "driver"


class DriverUpdateView(SuccessMessageMixin, UpdateView):
    model = Driver
    template_name = "drivers/driver-create.html"
    form_class = DriverCreationForm
    success_message = "Driver has been changed"


class DriverDeleteView(SuccessMessageMixin, DeleteView):
    model = Driver
    template_name = "drivers/driver-delete.html"
    success_url = reverse_lazy("driver-list")
    success_message = "Driver has been deleted"


class DriverListView(ListView):
    model = Driver
    template_name = "drivers/driver-list.html"
    context_object_name = 'drivers'
    paginate_by = 10
