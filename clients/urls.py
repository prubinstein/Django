from django.urls import path
from . import views

urlpatterns = [
    path('filter/', views.filter_clients, name='filter_clients'),
]
