# Generated by Django 2.2 on 2020-01-25 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prenda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingrediente',
            name='disponibilidad',
        ),
    ]
