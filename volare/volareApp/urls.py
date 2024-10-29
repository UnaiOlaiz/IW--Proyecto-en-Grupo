from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),    # pagina principal (index)
    path('paises/', views.index_Paises, name='index_paises'),   # lista de paises
    path('paises/<int:pais_id>/', views.show_Pais, name='show_pais'),   #detalles de pais
    path('aeropuertos', views.index_Aeropuerto, name='index_aeropuerto'),     # lista aeropuertos
    path('aeropuertos/<int:aeropuerto_id>/', views.show_Aeropuerto, name='show_aeropuerto'),    # detalles aeropuerto
    path('aerolineas/', views.index_Aerolineas, name='index_aerolineas'),   # lista aerolineas
    path('aerolineas/<int:aerolinea_id>/', views.show_Aerolinea, name='show_aerolinea'),    # detalles de una aerolinea
    
    # ??
    path('paises/<int:pais_id>/aerolineas/', views.index_Aerolineas_Pais, name='index_aerolineas_pais'),    # aerolineas de un pais
    path('paises/<int:aeropuerto_id>/aeropuertos/', views.index_Aeropuerto_Pais, name='index_aeropuerto'),     # aeropuertos de un pais


    path('airline/<str:airline_name>/', views.airline_detail, name='airline_detail'),
    path('country/<str:country_name>/', views.country_detail, name='country_detail'),  

]
