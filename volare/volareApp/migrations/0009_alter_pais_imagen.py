# Generated by Django 5.1.1 on 2024-11-15 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volareApp', '0008_alter_aerolinea_aeropuertos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='volareApp/css/imagenes/banderas', verbose_name='Image'),
        ),
    ]
