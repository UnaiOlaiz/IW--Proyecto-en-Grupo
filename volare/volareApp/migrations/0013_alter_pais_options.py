# Generated by Django 5.1.2 on 2024-12-01 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volareApp', '0012_alter_aerolinea_imagen_alter_aeropuerto_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pais',
            options={'permissions': [('puede_ver_pais', 'Puede ver la información de los países'), ('puede_editar_pais', 'Puede editar la información de los países')]},
        ),
    ]
