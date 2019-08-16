# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Genero
from app.services import Service
from app.functions import Function
from app.forms import GeneroForm

service = Service()
function = Function()

def radioonline_genero_list(request):
    generos = service.listarGeneros("")
    return render(request, 'generos/genero_list.html', {'generos':generos})

def radioonline_genero_view(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            message_text = "El genero fue registrado"
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect("radioonline_genero_list")
    else:
        return render(request, 'generos/genero_form.html', {'form':GeneroForm(),'nuevo':True})

def radioonline_genero_edit(request,id_genero):
    genero = get_object_or_404(Genero, id=id_genero)
    if request.method == 'GET':
        form = GeneroForm(instance=genero)
    else:
        form = GeneroForm(request.POST,instance=genero)
        if form.is_valid():
            form.save()
            message_text = "El genero fue actualizado"
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect("radioonline_genero_list")                  
        else:
            message_text = "Faltan datos para actualizar el genero"
            messages.add_message(request, messages.WARNING,message_text)  
            return redirect("radioonline_genero_edit",id_genero)    
    return render(request,'generos/genero_form.html',{'form':form,'genero':genero})

def radioonline_genero_delete(request,id_genero):
    genero = get_object_or_404(Genero, id=id_genero)
    if request.method == 'POST':
        if 'borrar_genero' in request.POST:
            genero.delete()
            message_text = "El genero fue borrado"
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect('radioonline_genero_list')
        elif 'volver_lista' in request.POST:
            return redirect('radioonline_genero_list')    
    return render(request,'generos/genero_delete.html',{'genero':genero})