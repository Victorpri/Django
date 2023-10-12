from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader


class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido



def saludo(request):  #primera  vista

    p1=Persona("Jose Arturo", "Alfonzo Lopez")

    #nombre="Victor"                 #se puede hacer uso de las variables para incocarlas en la plantilla con una variable o directamente
    #apellido="Prieto"              #colocando el calor de la clave en el diccionario o en el ctx=Context eje: "apellido_persona": "Prieto"

    temasDelCurso=["lo mismo1", "lo mimso 2"]
    listaVacia=[]

    ahora=datetime.datetime.now()

    doc_externo=open("C:/Users/Aprendiz/Desktop/Django/eje1/primerProyecto/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona": p1.nombre,                       #si se sacan los valores de una clase se debe de tener una variable donde se invoque esa clase y se llenen todos los parametros EJE: p1=Persona("Jose Arturo", "Alfonzo Lopez")
                 "apellido_persona": p1.apellido,
                 "momento_actual": ahora,
                 "temas":["plantillas","Modelos","Formularios", "Vistas","Desploegue"],     #una clave puede tener diferntes valores, esto se hace con una lista EJE: <-------  .I.
                 "remasDos": temasDelCurso,             #tambien se puede con un alista afuera del Context y se invoca adentro 
                 "Vacio": listaVacia})     
              

    documento=plt.render(ctx)

    return HttpResponse(documento)

#################################################################################################################################
#    LA DE ABAJO ES UNA FORMA MUCHO MAS ELEGANTE Y SIMPLE                                                                       #
#################################################################################################################################



def saludoDos(request):  #primera  vista

    p1=Persona("Jose Arturo", "Alfonzo Lopez")

    #nombre="Victor"                 #se puede hacer uso de las variables para incocarlas en la plantilla con una variable o directamente
    #apellido="Prieto"              #colocando el calor de la clave en el diccionario o en el ctx=Context eje: "apellido_persona": "Prieto"

    temasDelCurso=["lo mismo1", "lo mimso 2"]
    listaVacia=[]

    ahora=datetime.datetime.now()

    doc_externo=loader.get_template('miplantilla.html')  #necesitamos importar el loader el cual tengra dentro el get_template (mirar la seccion de templates en settings.py)

    documento=doc_externo.render({"nombre_persona": p1.nombre,                       
                 "apellido_persona": p1.apellido,               #si se sacan los valores de una clase se debe de tener una variable donde se invoque esa clase y se llenen todos los parametros EJE: p1=Persona("Jose Arturo", "Alfonzo Lopez")
                 "momento_actual": ahora,
                 "temas":["plantillas","Modelos","Formularios", "Vistas","Desploegue"],     #una clave puede tener diferntes valores, esto se hace con una lista EJE: <-------  .I.
                 "remasDos": temasDelCurso,             #tambien se puede con un alista afuera del Context y se invoca adentro 
                 "Vacio": listaVacia})

    return HttpResponse(documento)


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

