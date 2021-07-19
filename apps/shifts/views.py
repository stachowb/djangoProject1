from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ShiftCreationForm
from .models import Shift


class ShiftCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Shift
    form_class = ShiftCreationForm
    template_name = "shifts/shift-create.html"
    success_message = "Shift has been created"


class ShiftDetailsView(LoginRequiredMixin, DetailView):
    model = Shift
    template_name = "shifts/shift-details.html"
    context_object_name = "shift"


class ShiftUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Shift
    form_class = ShiftCreationForm
    success_message = "Shift has been updated"
    template_name = "shifts/shift-edit.html"


class ShiftDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Shift
    template_name = "shifts/shift-delete.html"
    success_message = "Shift has been deleted"
    success_url = reverse_lazy("shifts-list")


class ShiftListView(LoginRequiredMixin, ListView):
    model = Shift
    template_name = "shifts/shift-list.html"
    paginate_by = 50
    context_object_name = 'shifts'