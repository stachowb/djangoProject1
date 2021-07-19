from django.urls import path
from .views import ShiftCreateView, ShiftDetailsView, ShiftUpdateView, ShiftDeleteView, ShiftListView


urlpatterns =[
    path('create/', ShiftCreateView.as_view(), name='shift-create'),
    path('view/<slug:slug>', ShiftDetailsView.as_view(), name='shift-view'),
    path('edit/<slug:slug>', ShiftUpdateView.as_view(), name="shift-edit"),
    path('delete/<slug:slug>', ShiftDeleteView.as_view(), name='shift-delete'),
    path('', ShiftListView.as_view(), name='shift-list')
]