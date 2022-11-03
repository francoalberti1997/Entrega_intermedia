from django.shortcuts import render, HttpResponse, redirect
from PrimeraApp import models
from .forms import InputingForms


def padre(request) :
    return HttpResponse(f"hola")

def contacto(request):
    if request.method == "POST":
        mi_formulario = InputingForms(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario = models.Usuarios(nombre = data["nombre"], apellido = data["apellido"], contraseña = data["contraseña"])
            usuario.save()
            return redirect("home")

    else:
        mi_formulario = InputingForms()

    return render(request, "PrimeraApp/contacto.html", {"form":mi_formulario})


def home(request):
    experiencias =models.Experiencias.objects.all
    criterio = "3"    

    if request.GET["nombre"]:
        mi_formulario = InputingForms(request.POST)
        
        nombre = request.GET["nombre"]
        usuario = models.Usuarios.objects.filter(nombre___icontains = nombre)

        print(nombre, "aca mira")
        return render(request, "PrimeraApp/ingreso.html", {"nombres":nombre, "usuarios":usuario})


    else:
        mi_formulario = InputingForms()

    return render(request, "PrimeraApp/home.html", {"experiencias":experiencias, "criterio":criterio, "form":mi_formulario})


def ingreso(request) :

    informacion = request.GET["nombre"] #trabajando en que información, el nombrey contraseña introducido matcheen con la DB (usuarios), usar filter
    contraseña = request.GET["contraseña"] 
    usuarios = models.Usuarios.objects.all
    pass
