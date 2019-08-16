# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Emisora
from app.services import Service
from app.functions import Function
from app.forms import EmisoraForm

service = Service()
function = Function()

def radioonline_emisora_list(request):
    emisoras = service.listarEmisoras("")
    return render(request, 'emisoras/emisora_list.html', {'emisoras':emisoras})

def radioonline_emisora_view(request):
    if request.method == 'POST':
        form = EmisoraForm(request.POST)
        if form.is_valid():
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
            form.save()
            message_text = "La emisora fue editada"
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect("radioonline_emisora_list")                  
        else:
            message_text = "Faltan datos para registrar la emisora"
            messages.add_message(request, messages.WARNING,message_text)  
            return redirect("radioonline_emisora_edit",id_categoria)    
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