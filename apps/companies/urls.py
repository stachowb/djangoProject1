from django.urls import path
from .views import CompanyCreateView, CompanyListView, CompanyDetailView, CompanyUpdateView, CompanyDeleteView

urlpatterns = [
    path("create/", CompanyCreateView.as_view(), name="company-create"),
    path("", CompanyListView.as_view(), name="company-list"),
    path("view/<slug:slug>/", CompanyDetailView.as_view(), name="company-view"),
    path("edit/<slug:slug>", CompanyUpdateView.as_view(), name="company-edit"),
    path("delete/<slug:slug>", CompanyDeleteView.as_view(), name="company-delete")
]
