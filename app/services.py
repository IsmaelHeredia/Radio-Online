# Written By Ismael Heredia in the year 2018

import os,time,datetime,re
from app.functions import Function
from app.models import Genero,Emisora

function = Function()

class Service(object):

    def listarGeneros(self,patron):
        try:
            return Genero.objects.filter(nombre__icontains=patron).order_by('nombre')
        except Exception as e:
            pass

    def listarEmisoras(self,patron):
        try:
            return Emisora.objects.filter(nombre__icontains=patron).order_by('nombre')
        except Exception as e:
            pass

    def comprobar_existencia_genero_crear(self,nombre):
        response = False
        try:
            o = Genero.objects.get(nombre=nombre)
            response = True
        except Genero.DoesNotExist:
            response = False
        return response

    def comprobar_existencia_genero_editar(self,id,nombre):
        if Genero.objects.filter(nombre=nombre).exclude(id=id).exists():
            return True
        else:
            return False

    def comprobar_existencia_emisora_crear(self,nombre):
        response = False
        try:
            o = Emisora.objects.get(nombre=nombre)
            response = True
        except Emisora.DoesNotExist:
            response = False
        return response

    def comprobar_existencia_emisora_editar(self,id,nombre):
        if Emisora.objects.filter(nombre=nombre).exclude(id=id).exists():
            return True
        else:
            return False

    def destroy(self):
        pass