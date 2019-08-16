# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from django.conf import settings
from django.core.files import File
from django.http import JsonResponse
from app.services import Service
from app.functions import Function

service = Service()
function = Function()

def inicio(request):
  emisoras = service.listarEmisoras("")
  return render(request, 'home/index.html', {'emisoras':emisoras})