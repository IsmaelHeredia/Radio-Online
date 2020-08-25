# Written By Ismael Heredia in the year 2020

import os,time,datetime,re
from app.models import Emisora

class Service(object):

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