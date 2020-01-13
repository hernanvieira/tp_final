# Generated by Django 2.2 on 2020-01-10 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0005_delete_faltante'),
        ('prenda', '0008_auto_20191230_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faltante',
            fields=[
                ('id_faltante', models.AutoField(primary_key=True, serialize=False)),
                ('faltante', models.PositiveIntegerField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='material.Material')),
                ('prenda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prenda.Prenda')),
                ('tipo_material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='material.Tipo_material')),
            ],
            options={
                'verbose_name': 'Faltante',
                'verbose_name_plural': 'Faltantes',
                'ordering': ['id_faltante'],
            },
        ),
    ]
