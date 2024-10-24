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

    airlines_data = {
        'iberia': {
            'name': 'Iberia',
            'origin': 'España',
            'description': 'Iberia es la principal aerolínea de España, fundada en 1927. Ofrece vuelos internacionales y nacionales con una extensa red de rutas en Europa y América.',
            'airports': ['Aeropuerto Adolfo Suárez Madrid-Barajas', 'Aeropuerto de Barcelona-El Prat'],
            'fleet': {
                'total_planes': 118,
                'types': ['Airbus A319', 'Airbus A320', 'Airbus A321', 'Airbus A350'],
            },
            'services': ['Wi-Fi a bordo', 'Entretenimiento en vuelo', 'Comida y bebidas gratuitas'],
        },
        'air_europa': {
            'name': 'Air Europa',
            'origin': 'España',
            'description': 'Air Europa es una aerolínea española con sede en Mallorca. Es conocida por sus vuelos nacionales e internacionales, especialmente hacia destinos en América Latina.',
            'airports': ['Aeropuerto de Madrid-Barajas', 'Aeropuerto de Palma de Mallorca'],
            'fleet': {
                'total_planes': 40,
                'types': ['Boeing 787', 'Boeing 737'],
            },
            'services': ['Entretenimiento en vuelo', 'Comida y bebidas'],
        },
        'british_airways': {
            'name': 'British Airways',
            'origin': 'Reino Unido',
            'description': 'British Airways es la aerolínea bandera del Reino Unido. Ofrece vuelos a más de 200 destinos en todo el mundo desde su base principal en Londres.',
            'airports': ['Aeropuerto de Heathrow', 'Aeropuerto de Gatwick'],
            'fleet': {
                'total_planes': 254,
                'types': ['Airbus A320', 'Boeing 777', 'Boeing 787'],
            },
            'services': ['Wi-Fi a bordo', 'Salas VIP', 'Comida gourmet'],
        },
        'easyjet': {
            'name': 'EasyJet',
            'origin': 'Reino Unido',
            'description': 'EasyJet es una aerolínea de bajo coste británica, conocida por operar una amplia red de rutas en Europa, con un enfoque en la accesibilidad y los precios bajos.',
            'airports': ['Aeropuerto de Gatwick', 'Aeropuerto de Luton'],
            'fleet': {
                'total_planes': 323,
                'types': ['Airbus A319', 'Airbus A320'],
            },
            'services': ['Comida y bebidas a la venta', 'Check-in online gratuito'],
        },
        'lufthansa': {
            'name': 'Lufthansa',
            'origin': 'Alemania',
            'description': 'Lufthansa es la mayor aerolínea de Alemania y una de las principales en Europa. Ofrece una red global de vuelos, destacando en la calidad del servicio.',
            'airports': ['Aeropuerto de Fráncfort', 'Aeropuerto de Múnich'],
            'fleet': {
                'total_planes': 330,
                'types': ['Airbus A320', 'Boeing 747', 'Airbus A380'],
            },
            'services': ['Wi-Fi a bordo', 'Salas VIP', 'Comida gourmet'],
        },
        'germanwings': {
            'name': 'Germanwings',
            'origin': 'Alemania',
            'description': 'Germanwings es una aerolínea alemana de bajo coste, filial de Lufthansa, que opera principalmente vuelos dentro de Europa.',
            'airports': ['Aeropuerto de Colonia/Bonn', 'Aeropuerto de Stuttgart'],
            'fleet': {
                'total_planes': 38,
                'types': ['Airbus A319', 'Airbus A320'],
            },
            'services': ['Comida y bebidas a la venta'],
        },
        'air_france': {
            'name': 'Air France',
            'origin': 'Francia',
            'description': 'Air France es la aerolínea nacional de Francia, fundada en 1933. Ofrece vuelos a más de 200 destinos en todo el mundo, con énfasis en la calidad y el lujo.',
            'airports': ['Aeropuerto Charles de Gaulle', 'Aeropuerto de Niza-Costa Azul'],
            'fleet': {
                'total_planes': 228,
                'types': ['Airbus A320', 'Boeing 777', 'Airbus A350'],
            },
            'services': ['Wi-Fi a bordo', 'Entretenimiento en vuelo', 'Comida gourmet'],
        },
        'transavia': {
            'name': 'Transavia',
            'origin': 'Francia/Holanda',
            'description': 'Transavia es una aerolínea de bajo coste francesa y holandesa, operada por el grupo Air France-KLM. Se especializa en vuelos europeos a precios asequibles.',
            'airports': ['Aeropuerto de Ámsterdam Schiphol', 'Aeropuerto de París-Orly'],
            'fleet': {
                'total_planes': 40,
                'types': ['Boeing 737'],
            },
            'services': ['Comida y bebidas a la venta', 'Check-in online gratuito'],
        },
        'american_airlines': {
            'name': 'American Airlines',
            'origin': 'Estados Unidos',
            'description': 'American Airlines es una de las mayores aerolíneas del mundo, con sede en Texas. Ofrece una amplia red de rutas globales, especialmente en América del Norte y del Sur.',
            'airports': ['Aeropuerto de Dallas/Fort Worth', 'Aeropuerto de Miami'],
            'fleet': {
                'total_planes': 865,
                'types': ['Boeing 737', 'Airbus A321', 'Boeing 787'],
            },
            'services': ['Wi-Fi a bordo', 'Salas VIP', 'Comida y bebidas'],
        },
        'delta_airlines': {
            'name': 'Delta Airlines',
            'origin': 'Estados Unidos',
            'description': 'Delta Airlines es una de las aerolíneas más grandes de Estados Unidos, conocida por su extensa red de vuelos nacionales e internacionales.',
            'airports': ['Aeropuerto de Atlanta', 'Aeropuerto de Minneapolis-St. Paul'],
            'fleet': {
                'total_planes': 900,
                'types': ['Boeing 737', 'Airbus A320', 'Boeing 767'],
            },
            'services': ['Wi-Fi a bordo', 'Entretenimiento en vuelo', 'Comida y bebidas'],
        },
        'united_airlines': {
            'name': 'United Airlines',
            'origin': 'Estados Unidos',
            'description': 'United Airlines es una aerolínea estadounidense con sede en Chicago. Opera una extensa red de vuelos internacionales, siendo una de las aerolíneas fundadoras de Star Alliance.',
            'airports': ['Aeropuerto O\'Hare de Chicago', 'Aeropuerto de Newark'],
            'fleet': {
                'total_planes': 800,
                'types': ['Boeing 737', 'Airbus A320', 'Boeing 787'],
            },
            'services': ['Wi-Fi a bordo', 'Salas VIP', 'Comida y bebidas'],
        },
        'qantas': {
            'name': 'Qantas',
            'origin': 'Australia',
            'description': 'Qantas es la aerolínea nacional de Australia y una de las más antiguas del mundo, famosa por sus vuelos de larga distancia y su alta calidad de servicio.',
            'airports': ['Aeropuerto de Sídney', 'Aeropuerto de Melbourne'],
            'fleet': {
                'total_planes': 120,
                'types': ['Boeing 747', 'Airbus A330'],
            },
            'services': ['Wi-Fi a bordo', 'Salas VIP', 'Comida y bebidas'],
        },
        'virgin_australia': {
            'name': 'Virgin Australia',
            'origin': 'Australia',
            'description': 'Virgin Australia es la segunda aerolínea más grande de Australia. Ofrece vuelos dentro de Australia y hacia destinos internacionales cercanos.',
            'airports': ['Aeropuerto de Brisbane', 'Aeropuerto de Melbourne'],
            'fleet': {
                'total_planes': 30,
                'types': ['Boeing 737', 'Airbus A320'],
            },
            'services': ['Wi-Fi a bordo', 'Entretenimiento en vuelo', 'Comida y bebidas'],
        },
        'qatar_airways': {
            'name': 'Qatar Airways',
            'origin': 'Catar',
            'description': 'Qatar Airways es la aerolínea nacional de Catar y una de las más prestigiosas a nivel mundial, conocida por su servicio de lujo y su amplia red de destinos.',
            'airports': ['Aeropuerto Internacional Hamad'],
            'fleet': {
                'total_planes': 234,
                'types': ['Boeing 777', 'Airbus A350'],
            },
            'services': ['Wi-Fi a bordo', 'Salas VIP', 'Comida gourmet'],
        },
        'singapore_airlines': {
            'name': 'Singapore Airlines',
            'origin': 'Singapur',
            'description': 'Singapore Airlines es la aerolínea bandera de Singapur, famosa por su excepcional servicio al cliente y sus innovaciones en vuelos de larga distancia.',
            'airports': ['Aeropuerto Changi de Singapur'],
            'fleet': {
                'total_planes': 137,
                'types': ['Airbus A380', 'Boeing 777'],
            },
            'services': ['Wi-Fi a bordo', 'Salas VIP', 'Comida gourmet'],
        },
        'emirates': {
            'name': 'Emirates',
            'origin': 'Emiratos Árabes Unidos',
            'description': 'Emirates es la aerolínea nacional de Dubái, Emiratos Árabes Unidos, y es conocida por su lujo y su amplia red de vuelos intercontinentales.',
            'airports': ['Aeropuerto Internacional de Dubái'],
            'fleet': {
                'total_planes': 264,
                'types': ['Airbus A380', 'Boeing 777'],
            },
            'services': ['Wi-Fi a bordo', 'Salas VIP', 'Comida gourmet'],
        }
    }

    airline = airlines_data.get(airline_name, None)

    if airline:
        return render(request, 'airline_detail.html', {'airline': airline})
    else:
        # Manejo de errores en caso de que la aerolínea no exista
        return render(request, '404.html', status=404)

        
        
def country_detail(request, country_name): 
    countries_data = {
        'spain': {
            'name': 'España',
            'capital': 'Madrid',
            'description': 'España es conocida por su rica historia, cultura vibrante y hermosas playas. Destinos turísticos destacados incluyen Barcelona, Sevilla y Valencia.',
            'airports': ['Aeropuerto Adolfo Suárez Madrid-Barajas', 'Aeropuerto de Barcelona-El Prat'],
            'tourist_sites': ['La Sagrada Familia', 'Alhambra', 'Museo del Prado'],
            'flights_info': {
                'major_airlines': ['Iberia', 'Vueling', 'Air Europa'],
                'flight_destinations': ['Reino Unido', 'Francia', 'Italia'],
            },
        },
        'england': {
            'name': 'Inglaterra',
            'capital': 'Londres',
            'description': 'Inglaterra es famosa por su historia, cultura y arquitectura. Londres, la capital, alberga numerosos museos y sitios históricos.',
            'airports': ['Aeropuerto de Heathrow', 'Aeropuerto de Gatwick'],
            'tourist_sites': ['Torre de Londres', 'Puente de la Torre', 'British Museum'],
            'flights_info': {
                'major_airlines': ['British Airways', 'EasyJet', 'Ryanair'],
                'flight_destinations': ['España', 'Francia', 'Alemania'],
            },
        },
        'germany': {
            'name': 'Alemania',
            'capital': 'Berlín',
            'description': 'Alemania es conocida por su rica historia, castillos y ciudades vibrantes. Berlín es famosa por su historia cultural y política.',
            'airports': ['Aeropuerto de Berlín-Tegel', 'Aeropuerto de Múnich'],
            'tourist_sites': ['Puerta de Brandeburgo', 'Castillo de Neuschwanstein', 'Murallas de Berlín'],
            'flights_info': {
                'major_airlines': ['Lufthansa', 'Germanwings', 'Eurowings'],
                'flight_destinations': ['Francia', 'Reino Unido', 'Italia'],
            },
        },
        'france': {
            'name': 'Francia',
            'capital': 'París',
            'description': 'Francia es famosa por su arte, gastronomía y arquitectura. París, la capital, es un importante centro cultural y turístico.',
            'airports': ['Aeropuerto Charles de Gaulle', 'Aeropuerto de Niza-Costa Azul'],
            'tourist_sites': ['Torre Eiffel', 'Museo del Louvre', 'Palacio de Versalles'],
            'flights_info': {
                'major_airlines': ['Air France', 'EasyJet', 'Ryanair'],
                'flight_destinations': ['Alemania', 'Reino Unido', 'España'],
            },
        },
        'qatar': {
            'name': 'Catar',
            'capital': 'Doha',
            'description': 'Catar es un país pequeño pero rico, conocido por su moderna arquitectura y su hospitalidad. Doha es el principal centro comercial y cultural.',
            'airports': ['Aeropuerto Internacional Hamad'],
            'tourist_sites': ['Museo de Arte Islámico', 'Corniche de Doha', 'Souq Waqif'],
            'flights_info': {
                'major_airlines': ['Qatar Airways'],
                'flight_destinations': ['Emiratos Árabes Unidos', 'Bahréin', 'Arabia Saudita'],
            },
        },
        'uae': {
            'name': 'Emiratos Árabes Unidos',
            'capital': 'Abu Dabi',
            'description': 'Los Emiratos Árabes Unidos son famosos por sus lujosos rascacielos y destinos turísticos como Dubái y Abu Dabi.',
            'airports': ['Aeropuerto Internacional de Dubái', 'Aeropuerto Internacional de Abu Dabi'],
            'tourist_sites': ['Burj Khalifa', 'Palacio de los Emiratos', 'Desierto de Rub al-Jali'],
            'flights_info': {
                'major_airlines': ['Emirates', 'Etihad Airways'],
                'flight_destinations': ['India', 'Reino Unido', 'Tailandia'],
            },
        },
        'singapore': {
            'name': 'Singapur',
            'capital': 'Singapur',
            'description': 'Singapur es una ciudad-estado conocida por su limpieza, seguridad y diversidad cultural. Es un importante centro financiero y de transporte en Asia.',
            'airports': ['Aeropuerto Changi de Singapur'],
            'tourist_sites': ['Gardens by the Bay', 'Marina Bay Sands', 'Sentosa'],
            'flights_info': {
                'major_airlines': ['Singapore Airlines', 'SilkAir'],
                'flight_destinations': ['Malasia', 'Indonesia', 'Australia'],
            },
        },
        'australia': {
            'name': 'Australia',
            'capital': 'Canberra',
            'description': 'Australia es conocida por sus impresionantes paisajes, fauna única y ciudades vibrantes. Sydney y Melbourne son destinos populares.',
            'airports': ['Aeropuerto de Sídney', 'Aeropuerto de Melbourne'],
            'tourist_sites': ['Ópera de Sídney', 'Gran Barrera de Coral', 'Uluru'],
            'flights_info': {
                'major_airlines': ['Qantas', 'Virgin Australia'],
                'flight_destinations': ['Nueva Zelanda', 'Estados Unidos', 'Japón'],
            },
        },
        'united_states': {
            'name': 'Estados Unidos',
            'capital': 'Washington D.C.',
            'description': 'Los Estados Unidos son un país diverso con una mezcla de culturas, paisajes y ciudades icónicas. Nueva York y Los Ángeles son solo algunas de las ciudades destacadas.',
            'airports': ['Aeropuerto Internacional de Los Ángeles', 'Aeropuerto Internacional de O\'Hare'],
            'tourist_sites': ['Estatua de la Libertad', 'Parque Nacional de Yellowstone', 'Disneyland'],
            'flights_info': {
                'major_airlines': ['American Airlines', 'Delta Airlines', 'United Airlines'],
                'flight_destinations': ['Canadá', 'México', 'Europa'],
            },
        },
    
}
    country = countries_data.get(country_name, None)

    if country:
        return render(request, 'country_detail.html', {'country': country})
    else:
        # Manejo de errores en caso de que el país no exista
        return render(request, '404.html', status=404)
 