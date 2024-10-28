# Generated by Django 5.1.1 on 2024-10-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volareApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aerolinea',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='aeropuerto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='pais',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Image'),
        ),
    ]
