from django.http import HttpResponse
import datetime

def saludo(request):  #primera  vista
    
    return HttpResponse("Hola Mundo")

def despedida(request):
    return HttpResponse("adios mundo")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request,edad, age):
    

    periodo=age-2019
    edadFutura=edad+periodo
    documento="""<html>
    <body>
    <h1>
    En el año %s tendras %s años 
    </h1>
    </body>
    </html>""" % (age, edadFutura)
    
    return HttpResponse(documento)

