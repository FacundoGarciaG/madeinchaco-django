# Generated by Django 3.2.5 on 2021-07-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionMICH', '0005_alter_contenidos_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'contacto',
                'verbose_name_plural': 'contenidos',
            },
        ),
    ]
