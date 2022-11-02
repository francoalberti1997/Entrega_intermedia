from django.shortcuts import render, HttpResponse, redirect
from PrimeraApp import models
from .forms import InputingForms


def padre(request) :
    return render(request, "PrimeraApp/padre.html")



def home(request):
    experiencias =models.Experiencias.objects.all
    criterio = "3"
    return render(request, "PrimeraApp/home.html", {"experiencias":experiencias, "criterio":criterio})


def ingreso(request) :

    pass

    return render(request, "PrimeraApp/ingreso.html")

def formulario(request):

    if request.method == "POST":
        mi_formulario = InputingForms(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario = models.Usuarios(nombre = mi_formulario["nombre"], apellido = mi_formulario["apellido"], contraseña = mi_formulario["contraseña"])
            usuario.save()
            return redirect("Formularios")

    else:
        mi_formulario = InputingForms()
    
    return render(request, "PrimeraApp/formularios.html", {"form":mi_formulario})

