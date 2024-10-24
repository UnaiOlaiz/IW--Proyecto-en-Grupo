from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Pais, Aerolinea, Aeropuerto

def index(request):
    aerolineas = get_list_or_404(Aerolinea.objects.order_by('nombre'))
    context = {'lista_aerolineas': aerolineas}
    return render(request, 'index.html', context)

def index_Paises(request):
    paises = get_list_or_404(Pais.objects.order_by('nombre'))
    context = {'lista_paises': paises}
    return render(request, 'paises.html', context)

def show_Pais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    context = {'pais': pais}
    return render(request, 'pais_detail.html', context)

def index_Aeropuerto(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    aeropuertos = pais.aeropuerto_set.all()
    context = {'pais': pais, 'lista_aeropuertos': aeropuertos}
    return render(request, 'aeropuertos.html', context)

def show_Aeropuerto(request, aeropuerto_id):
    aeropuerto = get_object_or_404(Aeropuerto, pk=aeropuerto_id)
    context = {'aeropuerto': aeropuerto}
    return render(request, 'aeropuerto_detail.html', context)

def index_Aerolineas(request):
    aerolineas = get_list_or_404(Aerolinea.objects.order_by('nombre'))
    context = {'lista_aerolineas': aerolineas}
    return render(request, 'aerolineas.html', context)

def show_Aerolinea(request, aerolinea_id):
    aerolinea = get_object_or_404(Aerolinea, pk=aerolinea_id)
    context = {'aerolinea': aerolinea}
    return render(request, 'aerolinea_detail.html', context)

def index_Aerolineas_Pais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    aerolineas = pais.aerolinea_set.all()
    context = {'pais': pais, 'lista_aerolineas': aerolineas}
    return render(request, 'aerolineas_por_pais.html', context)


