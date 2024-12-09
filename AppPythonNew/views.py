from django.http import HttpResponse
from django.template import Template , Context
import datetime as dt
import random

def bienvenida(request):
    return HttpResponse("Hola, bienvenidos a mi sitio web de Iphones")

def hora_actual(request):

    ahora = dt.datetime.now()

    mensaje = f"La hora actual es {ahora.hour} : {ahora.minute}"

    return HttpResponse(mensaje)

def saludar(request, nombre, apellido):

    mensaje = f"Hola {nombre} {apellido} Mucho Gusto !!"

    return HttpResponse(mensaje)

# def inicio(request):

#     # SIEMPRE QUE COPIAMOS UNA RUTA TENEMOS QUE AGREGAR LA R AL PRINCIPIO O SINO TODAS LAS BARRAS TIENEN QUE ESTAR COPIADAS PARA EL LADO CONTRARIO /
#     f = open(r"C:\Apps Visual Studio Code\AppPython\AppPythonNew\AppPythonNew\templates\inicio.html")

#     plantilla = Template(f.read())
    
#     f.close()

#     aleatorio = random.randint(1, 100)

#     info = {"numero":aleatorio}

#     contexto = Context(info)

#     plantilla = plantilla.render(contexto)

#     return HttpResponse(plantilla)