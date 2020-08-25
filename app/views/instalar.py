# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from django.conf import settings
from django.core.files import File
from django.http import JsonResponse
from app.models import Emisora

def radioonline_instalar(request):

  #Rock

  Emisora.objects.create(nombre="Alternative Rock",url="http://7579.live.streamtheworld.com:80/977_ALTERN_SC",generos="Rock")
  Emisora.objects.create(nombre="Bulldogs-Radio",url="http://198.58.98.83:8062/stream",generos="Rock, Heavy Metal")
  Emisora.objects.create(nombre="Classic Rock 2",url="http://7599.live.streamtheworld.com:80/977_CLASSROCK_SC",generos="Rock")
  Emisora.objects.create(nombre="Classic Rock Florida HD",url="http://198.58.98.83:8258/stream",generos="Rock")
  Emisora.objects.create(nombre="KNKl Pirate Radio Sturgis",url="http://us4.internet-radio.com:8223/stream",generos="Rock")
  Emisora.objects.create(nombre="Meat Liquor",url="http://uk1.internet-radio.com:8011/stream",generos="Rock")
  Emisora.objects.create(nombre="San Franciscos 70s HITS",url="http://198.178.123.17:10922/stream",generos="Rock, Oldies")
  Emisora.objects.create(nombre="Magic 80s Florida",url="http://airspectrum.cdnstream1.com:8018/1606_192",generos="Rock, Oldies")
  Emisora.objects.create(nombre="Radio Bloodstream",url="http://uk1.internet-radio.com:8294/stream",generos="Rock, Metal")
  Emisora.objects.create(nombre="Hard Rock Radio Live",url="http://listen.radionomy.com/hardrockradioliveclassicrock",generos="Rock, Classic Rock")
  
  #Electronic

  Emisora.objects.create(nombre="#MUSIK.TECHHOUSE (PROGRESSIVE) - WWW.RAUTEMUSIK.FM - 24H MIXED PROGRESSIVE ELECTRO MINIMAL AND MORE!",url="http://techhouse-high.rautemusik.fm",generos="Techno")
  Emisora.objects.create(nombre="Eye Of Destiny Radio",url="http://uk6.internet-radio.com:8428/stream",generos="Chillout")
  Emisora.objects.create(nombre="LOUNGE-RADIO.COM swiss made",url="http://77.235.42.90:80/stream",generos="Chillout")
  Emisora.objects.create(nombre="MoveDaHouse",url="http://212.71.250.12:8000/stream",generos="House")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : ALL THE HITS ALL THE TIME",url="http://uk6.internet-radio.com:8124/stream",generos="Dance")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : AMBIENT + CHILLOUT + RELAXATION",url="http://www.partyviberadio.com:8056/stream",generos="Meditation")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : DUBSTEP + TRAP + BASS",url="http://www.partyviberadio.com:8040/stream",generos="Dubstep")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : TECHNO + HOUSE + TRANCE + ELECTRONIC",url="http://www.partyviberadio.com:8046/stream",generos="Techno")
  Emisora.objects.create(nombre="PulseEDM Dance Music Radio",url="http://pulseedm.cdnstream1.com:8124/1373_128",generos="Dubstep")
  Emisora.objects.create(nombre="Radio Play Emotions",url="http://5.39.82.157:8054/stream",generos="Dubstep")
  Emisora.objects.create(nombre="SOUL CENTRAL RADIO",url="http://178.79.158.160:8179/stream",generos="Deep House")

  #Alternative

  Emisora.objects.create(nombre="The Zone- Dublin",url="http://uk1.internet-radio.com:8355/stream",generos="Alternative")

  #Classic

  Emisora.objects.create(nombre="Venice Classic Radio Italia",url="http://174.36.206.197:8000/stream",generos="Classical")
  
  #Jazz

  Emisora.objects.create(nombre="JAZZGROOVE.org",url="http://199.180.72.2:8015/stream",generos="Jazz")

  #Rap - Hip hop

  Emisora.objects.create(nombre="Faymus Radio",url="http://uk7.internet-radio.com:8078/stream",generos="Rap")
  Emisora.objects.create(nombre="HOT 108 JAMZ - #1 FOR HIP HOP - www.hot108.com (a Powerhitz.com station)",url="http://hot108jamz.hot108.com:4040",generos="Hip Hop")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : RAP + HIP HOP + TRAP + DUBSTEP",url="http://www.partyviberadio.com:8016/stream",generos="Rap, Hip Hop, Trap, Dubstep")
  Emisora.objects.create(nombre="Power 95 Bermuda",url="http://us3.internet-radio.com:8026/stream",generos="Hip Hop")
  Emisora.objects.create(nombre="Pigpen Radio",url="http://178.79.158.160:8213/stream",generos="Hip Hop")
  
  #Top 40

  Emisora.objects.create(nombre="Merge 104.8",url="http://212.71.250.12:8040/stream",generos="Top40")

  #Pop

  Emisora.objects.create(nombre="PopTron: Electro-Pop and Indie Dance Rock [SomaFM]",url="http://ice3.somafm.com/poptron-128-mp3",generos="Pop")
  Emisora.objects.create(nombre="Yabloki Radio",url="http://uk6.internet-radio.com:8365/stream",generos="Pop")

  return redirect("radioonline_emisora_list")