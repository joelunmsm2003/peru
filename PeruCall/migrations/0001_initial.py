# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agentes',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('anexo', models.IntegerField()),
                ('fono', models.IntegerField()),
                ('tiempo', models.TimeField()),
                ('atendidas', models.IntegerField()),
                ('contactadas', models.IntegerField()),
                ('estado', models.TextField()),
            ],
            options={
                'db_table': 'agentes',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campania',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('fecha_cargada', models.DateField(db_column='fecha cargada')),
                ('usuario', models.IntegerField()),
                ('estado', models.TextField()),
            ],
            options={
                'db_table': 'campania',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=11)),
                ('text', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'data',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('licencias', models.CharField(max_length=100)),
                ('mascaras', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'db_table': 'empresa',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'nivel',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
