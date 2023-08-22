from django.urls import path
from . import views

urlpatterns = [
    path('', views.filter_clients, name='client_ajax'),
    path('filter-ajax/', views.filter_clients_ajax, name='filter_clients_ajax'),
]
