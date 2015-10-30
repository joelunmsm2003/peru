# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Agentes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    anexo = models.IntegerField()
    fono = models.IntegerField()
    tiempo = models.TimeField()
    atendidas = models.IntegerField()
    contactadas = models.IntegerField()
    estado = models.TextField()

    class Meta:
        managed = True
        db_table = 'agentes'



class Campania(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha_cargada = models.DateField(db_column='fecha cargada')  # Field renamed to remove unsuitable characters.
    usuario = models.IntegerField()
    estado = models.TextField()

    class Meta:
        managed = True
        db_table = 'campania'


class Data(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    author = models.CharField(max_length=11)
    text = models.CharField(max_length=11)

    class Meta:
        managed = True
        db_table = 'data'

class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)  
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    licencias = models.CharField(max_length=100)
    mascaras = models.CharField(max_length=100)
    telefono = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'empresa'

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    licencias = models.CharField(max_length=100)
    mascaras = models.CharField(max_length=100)
    telefono = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'usuario'

class Nivel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'nivel'
