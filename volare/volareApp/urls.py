from django.urls import path
from . import views
from .views import AerolineaCreateView, PaisCreateView, AeropuertoCreateView


#urlpatterns = [
#    path('', views.index, name='index'),    
#    path('paises/', views.index_Paises, name='index_paises'),   
#    path('paises/<int:pais_id>/', views.show_Pais, name='show_pais'),   
#    path('aeropuertos/', views.index_Aeropuerto, name='index_aeropuerto'),     
#    path('aeropuertos/<int:aeropuerto_id>/', views.show_Aeropuerto, name='show_aeropuerto'),    
#    path('aerolineas/', views.index_Aerolineas, name='index_aerolineas'),   
#    path('aerolineas/<int:aerolinea_id>/', views.show_Aerolinea, name='show_aerolinea'),

#    path('aerolineas/nueva/', AerolineaCreateView.as_view(), name='formulario_aerolinea'),

#    path('paises/nuevo/', PaisCreateView.as_view(), name='formulario_pais'),
#    path('aeropuertos/nuevo/', AeropuertoCreateView.as_view(), name='formulario_aeropuerto'),   
    
#    path('formulario/lista/', views.lista_formularios, name='lista_formularios'),

    # Vue
#    path('vue/', views.vue_spa, name="vue_spa"),
#]



from django.urls import path
from .views import IndexView, PaisListView, PaisDetailView, AeropuertoListView, AeropuertoDetailView, AerolineaListView, AerolineaDetailView
from .views import PaisCreateView, AeropuertoCreateView, AerolineaCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),    
    path('paises/', PaisListView.as_view(), name='index_paises'),  
    path('paises/<int:pk>/', PaisDetailView.as_view(), name='show_pais'),   
    path('aeropuertos/', AeropuertoListView.as_view(), name='index_aeropuerto'),  
    path('aeropuertos/<int:pk>/', AeropuertoDetailView.as_view(), name='show_aeropuerto'),  
    path('aerolineas/', AerolineaListView.as_view(), name='index_aerolineas'),   
    path('aerolineas/<int:pk>/', AerolineaDetailView.as_view(), name='show_aerolinea'),
    path('paises/nuevo/', PaisCreateView.as_view(), name='formulario_pais'),
    path('aeropuertos/nuevo/', AeropuertoCreateView.as_view(), name='formulario_aeropuerto'),   
    path('aerolineas/nueva/', AerolineaCreateView.as_view(), name='formulario_aerolinea'),

    # Página de lista de formularios (sin cambios)
    path('formulario/lista/', views.lista_formularios, name='lista_formularios'),

    # API para obtener aerolíneas de un país (AJAX)
    path('api/country/<int:country_id>/airlines/', views.get_country_airlines, name='get_country_airlines'),

    # Vue SPA (sin cambios)
    path('vue/', views.vue_spa, name="vue_spa"),
]
