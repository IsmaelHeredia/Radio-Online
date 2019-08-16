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
from app.models import Genero,Emisora

service = Service()
function = Function()

def radioonline_default(request):

  Genero.objects.create(nombre="Rock")
  Genero.objects.create(nombre="Country")
  Genero.objects.create(nombre="Jazz")
  Genero.objects.create(nombre="Dance")
  Genero.objects.create(nombre="Top40")
  Genero.objects.create(nombre="Classic Rock")
  Genero.objects.create(nombre="Trance")
  Genero.objects.create(nombre="House")
  Genero.objects.create(nombre="Ambient")
  Genero.objects.create(nombre="Chillout")
  Genero.objects.create(nombre="Oldies")
  Genero.objects.create(nombre="Metal")
  Genero.objects.create(nombre="Techno")
  Genero.objects.create(nombre="Hip Hop")
  Genero.objects.create(nombre="Heavy Metal")
  Genero.objects.create(nombre="Meditation")
  Genero.objects.create(nombre="Pop")
  Genero.objects.create(nombre="Rap")
  Genero.objects.create(nombre="Instrumental")
  Genero.objects.create(nombre="Deep House")
  Genero.objects.create(nombre="Dubstep")
  Genero.objects.create(nombre="Alternative")
  Genero.objects.create(nombre="Classical")

  Emisora.objects.create(nombre="Classic Rock Florida HD",url="http://198.58.98.83:8258/stream",genero=Genero.objects.get(nombre="Rock"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="131 Rock",url="http://uk1.internet-radio.com:8036/stream",genero=Genero.objects.get(nombre="Rock"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Meat Liquor",url="http://uk1.internet-radio.com:8011/stream",genero=Genero.objects.get(nombre="Rock"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="AT Radio",url="http://uk6.internet-radio.com:8424/stream",genero=Genero.objects.get(nombre="Rock"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="KNKl Pirate Radio Sturgis",url="http://us4.internet-radio.com:8223/stream",genero=Genero.objects.get(nombre="Rock"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Classic Rock",url="http://7599.live.streamtheworld.com:80/977_CLASSROCK_SC",genero=Genero.objects.get(nombre="Rock"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Alternative Rock",url="http://7579.live.streamtheworld.com:80/977_ALTERN_SC",genero=Genero.objects.get(nombre="Rock"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Majestic Jukebox Radio #HIGH QUALITY SOUND",url="http://uk3.internet-radio.com:8405/stream",genero=Genero.objects.get(nombre="Country"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="JAZZGROOVE.org",url="http://199.180.72.2:8015",genero=Genero.objects.get(nombre="Jazz"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : ALL THE HITS ALL THE TIME",url="http://uk6.internet-radio.com:8124/stream",genero=Genero.objects.get(nombre="Dance"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Merge 104.8",url="http://212.71.250.12:8040/stream",genero=Genero.objects.get(nombre="Top40"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="CLASSIC ROCK RADIO HD",url="http://us1.internet-radio.com:8111/stream",genero=Genero.objects.get(nombre="Classic Rock"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Dance Attack FM - The best EDM",url="http://uk4.internet-radio.com:8049/stream",genero=Genero.objects.get(nombre="Trance"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="MoveDaHouse",url="http://212.71.250.12:8000/stream",genero=Genero.objects.get(nombre="House"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Buddhapillow Radio",url="http://uk3.internet-radio.com:8399/stream",genero=Genero.objects.get(nombre="Ambient"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : AMBIENT + CHILLOUT + RELAXATION",url="http://www.partyviberadio.com:8056/stream",genero=Genero.objects.get(nombre="Meditation"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Eye Of Destiny Radio",url="http://uk6.internet-radio.com:8428/stream",genero=Genero.objects.get(nombre="Chillout"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="LOUNGE-RADIO.COM swiss made",url="http://77.235.42.90:80/stream",genero=Genero.objects.get(nombre="Chillout"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Personal Favorites 60s/70s/80s/90s/More",url="http://45.79.186.124:8160/stream",genero=Genero.objects.get(nombre="Oldies"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="San Franciscos 70s HITS",url="http://198.178.123.17:10922/stream",genero=Genero.objects.get(nombre="Oldies"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Magic 80s Florida",url="http://airspectrum.cdnstream1.com:8018/1606_192",genero=Genero.objects.get(nombre="Oldies"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Radio Bloodstream",url="http://uk1.internet-radio.com:8294/live",genero=Genero.objects.get(nombre="Metal"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : TECHNO + HOUSE + TRANCE + ELECTRONIC",url="http://www.partyviberadio.com:8046/stream",genero=Genero.objects.get(nombre="Techno"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="#MUSIK.TECHHOUSE (PROGRESSIVE) - WWW.RAUTEMUSIK.FM - 24H MIXED PROGRESSIVE ELECTRO MINIMAL AND MORE!",url="http://techhouse-high.rautemusik.fm",genero=Genero.objects.get(nombre="Techno"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Pigpen Radio",url="http://178.79.158.160:8213/stream",genero=Genero.objects.get(nombre="Hip Hop"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Power 95 Bermuda",url="http://us3.internet-radio.com:8026/stream",genero=Genero.objects.get(nombre="Hip Hop"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="TOPMOB RADIO",url="http://uk7.internet-radio.com:8297/stream",genero=Genero.objects.get(nombre="Hip Hop"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="HOT 108 JAMZ - #1 FOR HIP HOP - www.hot108.com (a Powerhitz.com station)",url="http://hot108jamz.hot108.com:4040",genero=Genero.objects.get(nombre="Hip Hop"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Bulldogs-Radio",url="http://198.58.98.83:8062/stream",genero=Genero.objects.get(nombre="Heavy Metal"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Yabloki Radio",url="http://uk6.internet-radio.com:8365/stream",genero=Genero.objects.get(nombre="Pop"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="PopTron: Electro-Pop and Indie Dance Rock [SomaFM]",url="http://ice3.somafm.com/poptron-128-mp3",genero=Genero.objects.get(nombre="Pop"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : RAP + HIP HOP + TRAP + DUBSTEP",url="http://www.partyviberadio.com:8016/stream",genero=Genero.objects.get(nombre="Rap"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Faymus Radio",url="http://uk7.internet-radio.com:8078/stream",genero=Genero.objects.get(nombre="Rap"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="The Grammar Club Radio",url="http://us4.internet-radio.com:8212/stream",genero=Genero.objects.get(nombre="Rap"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Music Lake - Relaxation Music, Meditation, Focus, Chill, Nature Sounds",url="http://50.7.68.251:7168/stream",genero=Genero.objects.get(nombre="Instrumental"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="SOUL CENTRAL RADIO",url="http://178.79.158.160:8179/stream",genero=Genero.objects.get(nombre="Deep House"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="PARTY VIBE RADIO : DUBSTEP + TRAP + BASS",url="http://www.partyviberadio.com:8040/stream",genero=Genero.objects.get(nombre="Dubstep"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="PulseEDM Dance Music Radio",url="http://pulseedm.cdnstream1.com:8124/1373_128",genero=Genero.objects.get(nombre="Dubstep"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Radio Play Emotions",url="http://5.39.82.157:8054/stream",genero=Genero.objects.get(nombre="Dubstep"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="The Zone- Dublin",url="http://uk1.internet-radio.com:8355/stream",genero=Genero.objects.get(nombre="Alternative"),fecha_registro="2019-03-30")
  Emisora.objects.create(nombre="Venice Classic Radio Italia",url="http://174.36.206.197:8000/stream",genero=Genero.objects.get(nombre="Classical"),fecha_registro="2019-03-30")

  emisoras = service.listarEmisoras("")

  return render(request, 'home/index.html', {'emisoras':emisoras})