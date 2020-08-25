# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from app.models import Emisora
import json
import os

def radioonline_emisora_exportar(request):
    emisoras = Emisora.objects.order_by('id')
    stations = []
    for emisora in emisoras:
        stations.append({
            "name" : emisora.nombre,
            "link" : emisora.url,
            "categories" : emisora.generos
        })
    filename = os.getcwd() + "\\app\\static\\downloads\\stations.json"
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, "w") as file:
        json.dump(stations, file, indent=2)
    return render(request, 'exportar/index.html')