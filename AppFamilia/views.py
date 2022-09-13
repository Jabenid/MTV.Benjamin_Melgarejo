from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse
from AppFamilia.models import Familia
# Create your views here.



def familia(resquest):

    Familiar1 = Familia(nombre="Damir",edad=0, cumpleaños="2022-5-26")
    
    Familiar1.save()

    Familiar2 = Familia(nombre="Angeles",edad=19, cumpleaños="2003-4-28")

    Familiar2.save()

    Familiar3 = Familia(nombre="Benjamin",edad=22, cumpleaños="2000-8-14")

    Familiar3.save()

    diccionario = {"FN1":Familiar1.nombre,"FN2": Familiar2.nombre,"FN3": Familiar3.nombre,"FE1":Familiar1.edad,"FE2":Familiar2.edad, "FE3":Familiar3.edad, "FC1":Familiar1.cumpleaños, "FC2":Familiar2.cumpleaños, "FC3":Familiar3.cumpleaños}

    miHtml = open("C:/Users/flaez/Desktop/Python CoderHouse/Desafio Familia/ProyectoFamilia/AppFamilia/templates/AppFamilia/familia.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)


    return HttpResponse(documento)




    
    

