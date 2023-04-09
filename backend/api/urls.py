# backend/api/urls.py

from django.urls import path
from .endpoints import views

app_name = 'api'

urlpatterns = [
    path('process_bond_data/', views.process_bond_data, name='process_bond_data'),
]
