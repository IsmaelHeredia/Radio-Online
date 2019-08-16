# Written By Ismael Heredia in the year 2018

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from app.views import home,generos,emisoras,instalar

urlpatterns = [

    url(r'^instalar/$',  instalar.radioonline_default, name='radioonline_default'),

    url(r'^$', home.inicio, name='inicio'),

    url(r'^generos/$',  generos.radioonline_genero_list, name='radioonline_genero_list'),
    url(r'^generos/agregar$', generos.radioonline_genero_view, name='radioonline_genero_view'),
    url(r'^generos/editar/(?P<id_genero>\d+)/$', generos.radioonline_genero_edit, name='radioonline_genero_edit'),
    url(r'^generos/borrar/(?P<id_genero>\d+)/$', generos.radioonline_genero_delete, name='radioonline_genero_delete'),

    url(r'^emisoras/$',  emisoras.radioonline_emisora_list, name='radioonline_emisora_list'),
    url(r'^emisoras/agregar$', emisoras.radioonline_emisora_view, name='radioonline_emisora_view'),
    url(r'^emisoras/editar/(?P<id_emisora>\d+)/$', emisoras.radioonline_emisora_edit, name='radioonline_emisora_edit'),
    url(r'^emisoras/borrar/(?P<id_emisora>\d+)/$', emisoras.radioonline_emisora_delete, name='radioonline_emisora_delete'),

]