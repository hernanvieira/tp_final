# Generated by Django 2.2 on 2020-01-23 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_historicalcliente_history_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalcliente',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
