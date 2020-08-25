# Written By Ismael Heredia in the year 2020

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from app.views import home,emisoras,instalar,importar,exportar

urlpatterns = [

    url(r'^instalar/$',  instalar.radioonline_instalar, name='radioonline_instalar'),

    url(r'^$', home.inicio, name='inicio'),

    url(r'^emisoras/$',  emisoras.radioonline_emisora_list, name='radioonline_emisora_list'),
    url(r'^emisoras/agregar$', emisoras.radioonline_emisora_view, name='radioonline_emisora_view'),
    url(r'^emisoras/editar/(?P<id_emisora>\d+)/$', emisoras.radioonline_emisora_edit, name='radioonline_emisora_edit'),
    url(r'^emisoras/borrar/(?P<id_emisora>\d+)/$', emisoras.radioonline_emisora_delete, name='radioonline_emisora_delete'),
    url(r'^emisoras/listaJson$', emisoras.radiooonline_emisora_json, name='radioonline_emisora_json'),
    url(r'^importar/$', importar.radioonline_emisora_importar, name='radioonline_emisora_importar'),
    url(r'^exportar/$', exportar.radioonline_emisora_exportar, name='radioonline_emisora_exportar'),

]