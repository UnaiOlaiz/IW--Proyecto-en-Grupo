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


def airline_detail(request, airline_name):
    # Aquí iría la lógica para obtener la aerolínea específica.
    # Por ejemplo, podrías buscar en una base de datos o usar un diccionario de aerolíneas.

    airlines_data = {
    'iberia': {
        'name': 'Iberia',
        'description': 'Iberia es la principal aerolínea de España, fundada en 1927. Ofrece vuelos internacionales y nacionales con una extensa red de rutas en Europa y América.',
    },
    'air_europa': {
        'name': 'Air Europa',
        'description': 'Air Europa es una aerolínea española con sede en Mallorca. Es conocida por sus vuelos nacionales e internacionales, especialmente hacia destinos en América Latina.',
    },
    'british_airways': {
        'name': 'British Airways',
        'description': 'British Airways es la aerolínea bandera del Reino Unido. Ofrece vuelos a más de 200 destinos en todo el mundo desde su base principal en Londres.',
    },
    'easyjet': {
        'name': 'EasyJet',
        'description': 'EasyJet es una aerolínea de bajo coste británica, conocida por operar una amplia red de rutas en Europa, con un enfoque en la accesibilidad y los precios bajos.',
    },
    'lufthansa': {
        'name': 'Lufthansa',
        'description': 'Lufthansa es la mayor aerolínea de Alemania y una de las principales en Europa. Ofrece una red global de vuelos, destacando en la calidad del servicio.',
    },
    'germanwings': {
        'name': 'Germanwings',
        'description': 'Germanwings es una aerolínea alemana de bajo coste, filial de Lufthansa, que opera principalmente vuelos dentro de Europa.',
    },
    'air_france': {
        'name': 'Air France',
        'description': 'Air France es la aerolínea nacional de Francia, fundada en 1933. Ofrece vuelos a más de 200 destinos en todo el mundo, con énfasis en la calidad y el lujo.',
    },
    'transavia': {
        'name': 'Transavia',
        'description': 'Transavia es una aerolínea de bajo coste francesa y holandesa, operada por el grupo Air France-KLM. Se especializa en vuelos europeos a precios asequibles.',
    },
    'american_airlines': {
        'name': 'American Airlines',
        'description': 'American Airlines es una de las mayores aerolíneas del mundo, con sede en Texas. Ofrece una amplia red de rutas globales, especialmente en América del Norte y del Sur.',
    },
    'delta_airlines': {
        'name': 'Delta Airlines',
        'description': 'Delta Airlines es una de las aerolíneas más grandes de Estados Unidos, conocida por su extensa red de vuelos nacionales e internacionales.',
    },
    'united_airlines': {
        'name': 'United Airlines',
        'description': 'United Airlines es una aerolínea estadounidense con sede en Chicago. Opera una extensa red de vuelos internacionales, siendo una de las aerolíneas fundadoras de Star Alliance.',
    },
    'qantas': {
        'name': 'Qantas',
        'description': 'Qantas es la aerolínea nacional de Australia y una de las más antiguas del mundo, famosa por sus vuelos de larga distancia y su alta calidad de servicio.',
    },
    'virgin_australia': {
        'name': 'Virgin Australia',
        'description': 'Virgin Australia es la segunda aerolínea más grande de Australia. Ofrece vuelos dentro de Australia y hacia destinos internacionales cercanos.',
    },
    'qatar_airways': {
        'name': 'Qatar Airways',
        'description': 'Qatar Airways es la aerolínea nacional de Catar y una de las más prestigiosas a nivel mundial, conocida por su servicio de lujo y su amplia red de destinos.',
    },
    'singapore_airlines': {
        'name': 'Singapore Airlines',
        'description': 'Singapore Airlines es la aerolínea bandera de Singapur, famosa por su excepcional servicio al cliente y sus innovaciones en vuelos de larga distancia.',
    },
    'emirates': {
        'name': 'Emirates',
        'description': 'Emirates es la aerolínea nacional de Dubái, Emiratos Árabes Unidos, y es conocida por su lujo y su amplia red de vuelos intercontinentales.',
    }
}


    airline = airlines_data.get(airline_name, None)

    if airline:
        return render(request, 'airline_detail.html', {'airline': airline})
    else:
        # Manejo de errores en caso de que la aerolínea no exista
        return render(request, '404.html', status=404)