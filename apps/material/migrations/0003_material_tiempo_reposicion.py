# Generated by Django 2.2 on 2019-12-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_auto_20191110_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='tiempo_reposicion',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
