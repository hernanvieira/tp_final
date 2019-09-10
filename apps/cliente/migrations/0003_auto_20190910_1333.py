# Generated by Django 2.2 on 2019-09-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20190910_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='activo',
            field=models.BooleanField(verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=100, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254, verbose_name='Correos'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='domicilio',
            field=models.TextField(blank=True, null=True, verbose_name='Domicilios'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name='Telefonos'),
        ),
    ]
