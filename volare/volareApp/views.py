
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Pais, Aerolinea, Aeropuerto
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import PaisForm, AeropuertoForm, AerolineaForm


# obtiene aerolinea y pais
#def index(request):
    # Obtener todos los países
#    paises = get_list_or_404(Pais.objects.order_by('nombre'))
    # País y su aerolínea más antigua
#    pais_aerolineas = {}

#    for pais in paises:
        # Obtener la aerolínea más antigua de cada país
#        aerolinea_antigua = pais.aerolinea_set.order_by('fundacion').first()
#        pais_aerolineas[pais] = aerolinea_antigua

#    context = {'pais_aerolineas': pais_aerolineas}
#    return render(request, 'index.html', context)

# Vista principal
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paises = Pais.objects.order_by('nombre')
        pais_aerolineas = {
            pais: pais.aerolinea_set.order_by('fundacion').first()
            for pais in paises
        }
        context['pais_aerolineas'] = pais_aerolineas
        return context


# Vista para obtener las aerolíneas de un país en formato JSON (para AJAX)
def get_country_airlines(request, country_id):
    """Devuelve las aerolíneas de un país en formato JSON."""
    pais = get_object_or_404(Pais, id=country_id)
    aerolineas = list(
        pais.aerolinea_set.values("id", "nombre", "fundacion", "imagen")
    )
    return JsonResponse({"aerolineas": aerolineas})


# Vista de listado de países
class PaisListView(ListView):
    model = Pais
    template_name = 'lista_pais.html'
    context_object_name = 'lista_paises'
    queryset = Pais.objects.order_by('nombre')


# Vista de detalle de país
class PaisDetailView(DetailView):
    model = Pais
    template_name = 'country_detail.html'
    context_object_name = 'pais'


# Vista de listado de aeropuertos
class AeropuertoListView(ListView):
    model = Aeropuerto
    template_name = 'lista_airport.html'
    context_object_name = 'lista_aeropuertos'
    queryset = Aeropuerto.objects.order_by('nombre')


# Vista de detalle de aeropuerto
class AeropuertoDetailView(DetailView):
    model = Aeropuerto
    template_name = 'airport_detail.html'
    context_object_name = 'aeropuerto'


# Vista de listado de aerolíneas
class AerolineaListView(ListView):
    model = Aerolinea
    template_name = 'lista_airline.html'
    context_object_name = 'lista_aerolineas'
    queryset = Aerolinea.objects.order_by('nombre')


# Vista de detalle de aerolínea
class AerolineaDetailView(DetailView):
    model = Aerolinea
    template_name = 'airline_detail.html'
    context_object_name = 'airline'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['airports'] = self.object.aeropuertos.all()
        return context


# Vista para crear un país
class PaisCreateView(CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'formulario_pais.html'
    success_url = reverse_lazy('formulario_pais')


# Vista para crear un aeropuerto
class AeropuertoCreateView(CreateView):
    model = Aeropuerto
    form_class = AeropuertoForm
    template_name = 'formulario_aeropuerto.html'
    success_url = reverse_lazy('formulario_aeropuerto')


# Vista para crear una aerolínea
class AerolineaCreateView(CreateView):
    model = Aerolinea
    form_class = AerolineaForm
    template_name = 'formulario_aerolinea.html'
    success_url = reverse_lazy('formulario_aerolinea')


# Vista de lista de formularios
def lista_formularios(request):
    return render(request, 'lista_formulario.html')


# Apartado Vue SPA
def vue_spa(request):
    return render(request, 'vue.html')
