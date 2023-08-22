from django.shortcuts import render
from django.http import JsonResponse
from clients.models import Client

def filter_clients(request):
    cities = Client.objects.values_list('city', flat=True).distinct()
    selected_city = request.GET.get('city', '')
    clients = Client.objects.all()
    if selected_city:
        clients = clients.filter(city=selected_city)
    
    return render(request, 'client_ajax/index.html', {'cities': cities, 'selected_city': selected_city, 'clients': clients})

def filter_clients_ajax(request):
    selected_city = request.GET.get('city', '')
    clientes = Client.objects.all()
    print(selected_city)
    if selected_city:
        clientes = clientes.filter(city = selected_city)  
    data = []
    for client in clientes:
        data.append({
            'name': client.name,
            'city': client.city,
        })
    
    return JsonResponse(data, safe=False)
