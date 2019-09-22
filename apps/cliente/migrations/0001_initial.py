# Generated by Django 2.2 on 2019-09-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='DNI')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefonos')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correos')),
                ('domicilio', models.TextField(blank=True, null=True, verbose_name='Domicilios')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['apellido'],
            },
        ),
    ]
