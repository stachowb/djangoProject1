from django.urls import path
from .views import DriverCreateView, DriverDetailView, DriverUpdateView, DriverDeleteView, DriverListView

urlpatterns = [
    path('create/', DriverCreateView.as_view(), name='driver-create'),
    path('view/<slug:slug>/', DriverDetailView.as_view(), name="driver-view"),
    path('edit/<slug:slug>/', DriverUpdateView.as_view(), name="driver-edit"),
    path('delete/<slug:slug>/', DriverDeleteView.as_view(), name="driver-delete"),
    path('', DriverListView.as_view(), name="driver-list"),
]