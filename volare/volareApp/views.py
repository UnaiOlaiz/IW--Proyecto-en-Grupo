from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Pais, Aerolinea, Aeropuerto

# obtiene aerolinea y pais
def index(request):
    
    # Obtener todos los países
    paises = get_list_or_404(Pais.objects.order_by('nombre'))
    # País y su aerolínea más antigua
    pais_aerolineas = {}
    
    for pais in paises:
        # Obtener la aerolínea más antigua de cada país
        aerolinea_antigua = pais.aerolinea_set.order_by('fundacion').first()
        pais_aerolineas[pais] = aerolinea_antigua

    context = {'pais_aerolineas': pais_aerolineas}
    return render(request, 'index.html', context)

# lista de paises
def index_Paises(request):
    paises = get_list_or_404(Pais.objects.order_by('nombre'))
    context = {'lista_paises': paises}
    return render(request, 'lista_pais.html', context)

# detalles de pais usando ID
def show_Pais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    context = {'pais': pais}
    return render(request, 'country_detail.html', context)

# lista de todos los aeropuertos
def index_Aeropuerto(request):
    aeropuertos = get_list_or_404(Aeropuerto.objects.order_by('nombre'))
    context = {'lista_aeropuertos': aeropuertos}
    return render(request, 'lista_airport.html', context)

# detalles de aeropuerto usando ID
def show_Aeropuerto(request, aeropuerto_id):
    aeropuerto = get_object_or_404(Aeropuerto, pk=aeropuerto_id)
    context = {'aeropuerto': aeropuerto}
    return render(request, 'airport_detail.html', context)

# lista aerolineas
def index_Aerolineas(request):
    aerolineas = get_list_or_404(Aerolinea.objects.order_by('nombre'))
    context = {'lista_aerolineas': aerolineas}
    return render(request, 'lista_airline.html', context)

# detalles de aerolinea usando ID
def show_Aerolinea(request, aerolinea_id):
    aerolinea = get_object_or_404(Aerolinea, pk=aerolinea_id)  # Obtener la aerolínea
    context = {
        'airline': aerolinea,
        'airports': aerolinea.aeropuertos.all()  # Obtener aeropuertos relacionados
    }
    return render(request, 'airline_detail.html', context)


