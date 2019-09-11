# Generated by Django 2.2 on 2019-09-11 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Unidad_medida',
            fields=[
                ('id_unidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_material',
            fields=[
                ('id_material', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField()),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Unidad_medida')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id_material', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('tipo_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Tipo_material')),
            ],
        ),
    ]
