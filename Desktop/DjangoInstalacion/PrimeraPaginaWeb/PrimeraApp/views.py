from django.shortcuts import render, HttpResponse
from PrimeraApp import models


def padre(request) :
    return render(request, "PrimeraApp/padre.html")



def home(request):
    experiencias =models.Experiencias.objects.all
    criterio = "3"
    return render(request, "PrimeraApp/home.html", {"experiencias":experiencias, "criterio":criterio})


def ingreso(request) :

    informacion = request.GET["nombre"] #trabajando en que información, el nombrey contraseña introducido matcheen con la DB (usuarios), usar filter
    contraseña = request.GET["contraseña"] 
    usuarios = models.Usuarios.objects.all

    return render(request, "PrimeraApp/ingreso.html", {"informacion":informacion, "usuarios":usuarios, "contraseña":contraseña})
