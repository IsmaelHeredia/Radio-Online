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

    def destroy(self):
        pass