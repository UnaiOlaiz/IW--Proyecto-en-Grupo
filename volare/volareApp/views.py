from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Pais, Aerolinea, Aeropuerto
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Llama al contexto original del TemplateView
        context = super().get_context_data(**kwargs)

        # Obtener todos los países
        paises = Pais.objects.order_by('nombre')
        
        # Crear un diccionario para guardar los países y su aerolínea más antigua
        pais_aerolineas = {}

        for pais in paises:
            # Obtener la aerolínea más antigua de cada país
            aerolinea_antigua = pais.aerolinea_set.order_by('fundacion').first()
            pais_aerolineas[pais] = aerolinea_antigua

        # Añadir el diccionario de pais_aerolineas al contexto
        context['pais_aerolineas'] = pais_aerolineas
        return context

# lista de paises
class PaisListView(ListView):
    model = Pais
    template_name = 'lista_pais.html'
    context_object_name = 'lista_paises'
    queryset = Pais.objects.order_by('nombre')

# detalles de pais 
class PaisDetailView(DetailView):
    model = Pais
    template_name = 'country_detail.html'
    context_object_name = 'pais'

# lista de todos los aeropuertos
class AeropuertoListView(ListView):
    model = Aeropuerto
    template_name = 'lista_airport.html'
    context_object_name = 'lista_aeropuertos'
    queryset = Aeropuerto.objects.order_by('nombre')

# detalles de aeropuerto 
class AeropuertoDetailView(DetailView):
    model = Aeropuerto
    template_name = 'airport_detail.html'
    context_object_name = 'aeropuerto'

# lista aerolineas
class AerolineaListView(ListView):
    model = Aerolinea
    template_name = 'lista_airline.html'
    context_object_name = 'lista_aerolineas'
    queryset = Aerolinea.objects.order_by('nombre')

# detalles de aerolinea 
class AerolineaDetailView(DetailView):
    model = Aerolinea
    template_name = 'airline_detail.html'
    context_object_name = 'airline'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['airports'] = self.object.aeropuertos.all()  # Relación de aeropuertos de la aerolínea
        return context

class PaisCreateView(CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'formulario_pais.html'
    success_url = reverse_lazy('formulario_pais')
    
class AeropuertoCreateView(CreateView):
    model = Aeropuerto
    form_class = AeropuertoForm
    template_name = 'formulario_aeropuerto.html'
    success_url = reverse_lazy('formulario_aeropuerto')
    
class AerolineaCreateView(CreateView):
    model = Aerolinea
    form_class = AerolineaForm
    template_name = 'formulario_aerolinea.html'
    success_url = reverse_lazy('formulario_aerolinea')


def lista_formularios(request):
    return render(request, 'lista_formulario.html')

# Apartado Vue SPA
def vue_spa(request):
    return render(request, 'vue.html')