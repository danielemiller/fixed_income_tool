# backend/api/urls.py

from django.urls import path
from .endpoints import process_bond_data, fetch_bond_data_list # Import process_bond_data directly

app_name = 'api'

urlpatterns = [
    path('process_bond_data/', process_bond_data, name='process_bond_data'),
    path('api/fetch_bond_data_list/', fetch_bond_data_list, name='fetch_bond_data_list'),
]

