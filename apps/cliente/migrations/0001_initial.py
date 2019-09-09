# Generated by Django 2.2 on 2019-09-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=200)),
                ('domicilio', models.TextField(blank=True, null=True)),
                ('activo', models.BooleanField()),
            ],
        ),
    ]
