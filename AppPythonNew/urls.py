"""
URL configuration for AppPythonNew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

## Username Admin Django Brunobm
## Email bruno.bonomo11@gmail.com
## Password Boca_201100

from django.contrib import admin
from django.urls import path
from .views import *
from AppProductos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", inicio),

    path("listadoCompus/", ver_computadoras, name="Computadoras"),
    path("listadoCelulares/", ver_celulares, name="Celulares"),
    path("listadoTelevisores/", ver_televisores, name="Televisores"),

    path("nuevaComputadora/", agregar_computadora),
    path("nuevoCelular/", agregar_celulares),
    path("nuevoTelevisor/", agregar_televisores),
]
