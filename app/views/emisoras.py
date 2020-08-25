# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Emisora
from app.forms import EmisoraForm
from django.core import serializers
from django.http import HttpResponse
from app.services import Service
import json
from django.core.serializers.json import DjangoJSONEncoder

service = Service()

def radioonline_emisora_list(request):
    emisoras = Emisora.objects.order_by('id')
    return render(request, 'emisoras/emisora_list.html', {'emisoras':emisoras})

def radioonline_emisora_view(request):
    if request.method == 'POST':
        form = EmisoraForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nombre = data["nombre"]
            if service.comprobar_existencia_emisora_crear(nombre):
                message_text = "La emisora "+nombre+" ya existe"
                messages.add_message(request, messages.WARNING,message_text)
                return redirect("radioonline_emisora_view")
            else:                
                form.save()
                message_text = "La emisora fue registrada"
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect("radioonline_emisora_list")
    else:
        return render(request, 'emisoras/emisora_form.html', {'form':EmisoraForm(),'nuevo':True})

def radioonline_emisora_edit(request,id_emisora):
    emisora = get_object_or_404(Emisora, id=id_emisora)
    if request.method == 'GET':
        form = EmisoraForm(instance=emisora)
    else:
        form = EmisoraForm(request.POST,instance=emisora)
        if form.is_valid():
            data = form.cleaned_data
            nombre = data["nombre"]
            if service.comprobar_existencia_emisora_editar(id_emisora,nombre):
                message_text = "El género "+nombre+" ya existe"
                messages.add_message(request, messages.WARNING,message_text)
                return redirect("radioonline_emisora_view")
            else:
                form.save()
                message_text = "La emisora fue editada"
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect("radioonline_emisora_list")                  
        else:
            message_text = "Faltan datos para registrar la emisora"
            messages.add_message(request, messages.WARNING,message_text)  
            return redirect("radioonline_emisora_edit",id_emisora)    
    return render(request,'emisoras/emisora_form.html',{'form':form,'emisora':emisora})

def radioonline_emisora_delete(request,id_emisora):
    emisora = get_object_or_404(Emisora, id=id_emisora)
    if request.method == 'POST':
        if 'borrar_emisora' in request.POST:
            emisora.delete()
            message_text = "La emisora fue borrada"
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect('radioonline_emisora_list')
        elif 'volver_lista' in request.POST:
            return redirect('radioonline_emisora_list')    
    return render(request,'emisoras/emisora_delete.html',{'emisora':emisora})

def radiooonline_emisora_json(request):
    lista = []
    emisoras = Emisora.objects.order_by('id')
    for emisora in emisoras:
        item = {}
        item["id"] = emisora.id
        item["nombre"] = emisora.nombre
        item["url"] = emisora.url
        item["generos"] = emisora.generos
        generos = emisora.generos
        generos = generos.replace(",","")
        item["string"] = emisora.nombre + " " + generos
        lista.append(item)
    json_data = json.dumps(list(lista), cls=DjangoJSONEncoder)
    return HttpResponse(json_data)