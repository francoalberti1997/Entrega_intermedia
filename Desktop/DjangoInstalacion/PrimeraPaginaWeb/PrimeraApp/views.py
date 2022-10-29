from django.shortcuts import render, HttpResponse
from PrimeraApp import models
from PrimeraApp.funciones import devuelve_buenas_experiencias

def padre(request) :
    return render(request, "PrimeraApp/padre.html")



def home(request):
    experiencias =models.Experiencias.objects.all
    criterio = "3"
    return render(request, "PrimeraApp/home.html", {"experiencias":experiencias, "criterio":criterio})


def ingreso(request) :

    informacion = request.GET["nombre"] #trabajando en que información, el nombrey contraseña introducido matcheen con la DB (usuarios), usar filter
    usuarios = models.Usuarios.objects.all

    if informacion in :
        return render(request, "PrimeraApp/ingreso.html", {"informacion":informacion})
    else:
        return HttpResponse("datos incorrectos")