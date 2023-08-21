from django.shortcuts import render
from .models import Client

def filter_clients(request):
    cities = Client.objects.values_list('city', flat=True).distinct()
    
    selected_city = request.GET.get('city', '')
    if selected_city:
        clients = Client.objects.filter(city=selected_city)
    else:
        clients = Client.objects.all()
    
    return render(request, 'clients/filter.html', {'cities': cities, 'selected_city': selected_city, 'clients': clients})
