# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from app.models import Emisora
import json

def radioonline_emisora_importar(request):
    if request.method == 'POST':
        if 'archivoJSON' in request.FILES:
            file = request.FILES['archivoJSON']
            content = file.read().decode()
            stations = json.loads(content)
            for station in stations:
                name = station["name"]
                link = station["link"]
                categories = station["categories"]
                emisora_object = Emisora()
                emisora_object.nombre = name
                emisora_object.url = link
                emisora_object.generos = categories
                emisora_object.save()
            message_text = "Datos importados"
            messages.add_message(request, messages.SUCCESS,message_text)  
        return render(request, 'importar/index.html')
    else:
        return render(request, 'importar/index.html')