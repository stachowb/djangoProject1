from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Company
from .forms import CompanyCreateForm


class CompanyCreateView(SuccessMessageMixin, CreateView):
    model = Company
    template_name = "companies/company-create.html"
    form_class = CompanyCreateForm
    success_message = "Company has been created"


class CompanyDetailView(DetailView):
    model = Company
    template_name = "companies/company-details.html"
    context_object_name = "company"


class CompanyListView(ListView):
    model = Company
    paginate_by = 10
    context_object_name = "companies"
    template_name = "companies/company-list.html"


class CompanyUpdateView(SuccessMessageMixin, UpdateView):
    model = Company
    template_name = "companies/company-create.html"
    form_class = CompanyCreateForm
    success_message = "Company has been changed"


class CompanyDeleteView(SuccessMessageMixin, DeleteView):
    model = Company
    template_name = "companies/company-delete.html"
    success_url = reverse_lazy("company-list")
    success_message = "Company has been deleted"
