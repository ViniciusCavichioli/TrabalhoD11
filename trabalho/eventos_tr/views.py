from django.shortcuts import render
from django.http import HttpResponse
from eventos_tr.models import *

def listaEvento(request):
    retorno = "<h1>Eventos</h1>"
    lista = Evento.objects.all()
    for evento in lista:
        retorno += '</br> Nome do Evento: {} </br>'.format(evento.nome)
    return HttpResponse(retorno)

def get_evento_byID(request, id):
    retorno = "<h1>Evento</h1>"
    evento = Evento.objects.get(pk = id)
    retorno = retorno + '</br> Nome do Evento: {}</br>'.format(evento.nome)
    return HttpResponse(retorno)

# Create your views here.
