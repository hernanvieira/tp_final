# Generated by Django 2.2 on 2020-01-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0004_auto_20200124_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='disponibilidad',
            field=models.CharField(default='', max_length=50),
        ),
    ]
