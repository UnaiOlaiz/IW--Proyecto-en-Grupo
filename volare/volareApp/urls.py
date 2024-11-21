from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('paises/', views.index_Paises, name='index_paises'),   
    path('paises/<int:pais_id>/', views.show_Pais, name='show_pais'),   
    path('aeropuertos/', views.index_Aeropuerto, name='index_aeropuerto'),     
    path('aeropuertos/<int:aeropuerto_id>/', views.show_Aeropuerto, name='show_aeropuerto'),    
    path('aerolineas/', views.index_Aerolineas, name='index_aerolineas'),   
    path('aerolineas/<int:aerolinea_id>/', views.show_Aerolinea, name='show_aerolinea'),  
]



