from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from volareApp.models import Aerolinea, Aeropuerto, Pais  # Cambia esto por el nombre correcto de tu aplicación y modelos

class Command(BaseCommand):
    help = 'Crea grupos de usuarios y asigna permisos a cada uno'

    def handle(self, *args, **kwargs):
        # Crea el grupo de administrador
        admin_group, created = Group.objects.get_or_create(name='Administrador')

        # Crea permisos específicos para Aerolinea, Aeropuerto y Pais
        aeropuerto_content_type = ContentType.objects.get_for_model(Aeropuerto)
        aerolinea_content_type = ContentType.objects.get_for_model(Aerolinea)
        pais_content_type = ContentType.objects.get_for_model(Pais)

        # Obtener los permisos (asegúrate de que estos permisos existan)
        permiso_aeropuerto = Permission.objects.get(
            codename='add_aeropuerto', content_type=aeropuerto_content_type)
        permiso_aerolinea = Permission.objects.get(
            codename='add_aerolinea', content_type=aerolinea_content_type)
        permiso_pais = Permission.objects.get(
            codename='add_pais', content_type=pais_content_type)

        # Asignar permisos al grupo
        admin_group.permissions.add(permiso_aeropuerto, permiso_aerolinea, permiso_pais)

        # Mensaje de éxito
        self.stdout.write(self.style.SUCCESS('Grupo de administrador creado con permisos asignados.'))
