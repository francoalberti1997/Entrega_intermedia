from django.shortcuts import render, HttpResponse, redirect
from PrimeraApp import models
from .forms import InputingForms


def padre(request) :
    return HttpResponse(f"hola")


def home(request):
    return HttpResponse(f"hola")


def ingreso(request) :
    return HttpResponse(f"hola")


def formulario(request):

    if request.method == "POST":
        mi_formulario = InputingForms(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario = models.Usuarios(nombre = data["nombre"], apellido = data["apellido"], contraseña = data["contraseña"])
            usuario.save()
            return redirect("Formularios")

    else:
        mi_formulario = InputingForms()
    
    return render(request, "PrimeraApp/formulario.html", {"form":mi_formulario})

