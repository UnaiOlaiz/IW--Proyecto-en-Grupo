# Generated by Django 4.2.16 on 2024-10-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volareApp', '0003_aerolinea_fundacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='aerolinea',
            name='descripcion',
            field=models.CharField(default='Sin descripción', max_length=255),
        ),
    ]
