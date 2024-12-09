from django.shortcuts import render
from django.http import HttpResponse
from AppProductos.models import Computadoras, Celulares, Televisores
from AppProductos.forms import ComputadoraFormulario

# Create your views here.

def inicio(request):

    return render(request, "AppProductos/inicio.html")


def ver_computadoras(request):

    mis_computadoras = Computadoras.objects.all()

    info = {"computadoras":mis_computadoras}

    return render(request, "AppProductos/computadoras.html", info)



def ver_celulares(request):

    mis_celulares = Celulares.objects.all()

    info = {"celulares":mis_celulares}

    return render(request, "AppProductos/celulares.html", info)



def ver_televisores(request):

    mis_televisores = Televisores.objects.all()

    info = {"televisores":mis_televisores}

    return render(request, "AppProductos/televisores.html", info)




def agregar_computadora(request):

    if request.method == "POST":

        nuevo_formulario = ComputadoraFormulario(request.POST)

        if nuevo_formulario.is_valid():

            computadora_nueva = Computadoras(nombre=info["nombre"], precio=info["precio"], marca=info["marca"], almacenamiento=info["almacenamiento"], proveedor=info["proveedor"])
            
            info = nuevo_formulario.cleaned_data

            computadora_nueva.save()

            return render(request, "AppProductos/inicio.html")
        
        else:

            nuevo_formulario = ComputadoraFormulario()
    
    return render(request, "AppProductos/formu_computadora.html", {"mi_formu":nuevo_formulario})
    
    
    # computadora1 = Computadoras(nombre="Computadora All In ONE White", precio=1560550, marca="HP Industry Argen", almacenamiento="1TB", proveedor="La Rioja S.A")
    # computadora1.save()

    # computadora2 = Computadoras(nombre="Computadora All In ONE Black", precio=1350000, marca="Haitech Industry Off", almacenamiento="512GB", proveedor="Intel Miami FL")
    # computadora2.save()

    # computadora3 = Computadoras(nombre="Computadora All In ONE Grey", precio=626000, marca="IPS Panel Off", almacenamiento="256GB", proveedor="Outdoor Australy PL")
    # computadora3.save()

    # computadora4 = Computadoras(nombre="Computadora All In ONE White/Grey", precio=1480000, marca="Lenovo", almacenamiento="512GB", proveedor="Lenovo S.A Argentina")
    # computadora4.save()

    # computadora5 = Computadoras(nombre="Computadora All In ONE Black/White", precio=850000, marca="Ryzen 5 Intel", almacenamiento="128GB", proveedor="Outdoor Australy PL")
    # computadora5.save()

    # computadora6 = Computadoras(nombre="Computadora All In ONE Grey", precio=2900000, marca="Dell", almacenamiento="2TB", proveedor="Outside Argentina S.A")
    # computadora6.save()




def agregar_celulares(request):

    celular_nuevo = Celulares(
        nombre=request.POST["nombre"],
        precio=request.POST["precio"],
        marca=request.PSOT["marca"],
        almacenamiento=request.POST["almacenamiento"],
        proveedor=request.POST["proveedor"]
    )

    celular_nuevo.save()

    
    
    return render(request, "AppProductos/nuevo_celular.html")


    # celular1 = Celulares(nombre="Iphone 13 Pro Max", precio=789000, marca="Apple", almacenamiento="128GB", proveedor="Apple INC S.A Sidney")
    # celular1.save()

    # celular2 = Celulares(nombre="Iphone 14", precio=850200, marca="Apple", almacenamiento="256GB", proveedor="Apple INC S.A Sidney")
    # celular2.save()

    # celular3 = Celulares(nombre="Iphone 14 Pro Max", precio=925000, marca="Apple", almacenamiento="512GB", proveedor="Apple INC S.A Sidney")
    # celular3.save()

    # celular4 = Celulares(nombre="Iphone 15 Pro Max", precio=1150000, marca="Apple", almacenamiento="256GB", proveedor="Apple INC S.A Sidney")
    # celular4.save()

    # celular5 = Celulares(nombre="Iphone 16", precio=960300, marca="Apple", almacenamiento="1TB", proveedor="Apple INC S.A Sidney")
    # celular5.save()

    # celular6 = Celulares(nombre="Iphone 16 Pro Max", precio=2100000, marca="Apple", almacenamiento="1TB", proveedor="Apple INC S.A Sidney")
    # celular6.save()




def agregar_televisores(request):

    televisor_nuevo = Televisores(
        nombre=request.POST["nombre"],
        precio=request.POST["precio"],
        marca=request.PSOT["marca"],
        almacenamiento=request.POST["almacenamiento"],
        proveedor=request.POST["proveedor"]
    )

    televisor_nuevo.save()

    
    
    return render(request, "AppProductos/nuevo_televisor.html")
    
    
    
    # televisor1 = Televisores(nombre="Smart TV Quint", precio= 499000, marca="Android", pulgadas= 50, proveedor="Android S.A Import")
    # televisor1.save()

    # televisor2 = Televisores(nombre="Samsung TV UHD", precio= 618000, marca="Samsung", pulgadas= 43, proveedor="Samsung S.A Argentina")
    # televisor2.save()

    # televisor3 = Televisores(nombre="Televisor TCL LED", precio= 285000, marca="TLC", pulgadas= 32, proveedor="TLC S.A Argentina")
    # televisor3.save()

    # televisor4 = Televisores(nombre="Samsung TV LED 4K", precio= 985000, marca="Samsung", pulgadas= 50, proveedor="Samsung S.A Argentina")
    # televisor4.save()

    # televisor5 = Televisores(nombre="Samsung TV QLED LITE 4K", precio= 1399999, marca="Samsung", pulgadas= 65, proveedor="Samsung S.A Argentina")
    # televisor5.save()

    # televisor6 = Televisores(nombre="Smart Tv Hisense Full HD", precio= 379000, marca="Hisense", pulgadas= 40, proveedor="Hisense S.A Argentina")
    # televisor6.save()
