from django.http import HttpResponse
from django.template import Template,Context
import datetime
from django.template.loader import get_template
from django.shortcuts import render
#El loader(loader.get_template) nos permite cargar plantillas de un directorio lin19
#Se activa en settings/DIRS entre ""
#cambiar el contexto a dictionary
class persona (object):
    def __init__(self,nombre,apellido):
        
        self.nombre=nombre

        self.apellido=apellido

def saludo(request):

    p1=persona("Profesor Manuel " , "Diaz")

    ahora=datetime.datetime.now()

    temas_del_curso=["Plantillas","Modelos","Formulario","Vistas","Despliegue"]    

    return render(request, 'doc.html',{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temas_del_curso})

def curso_c(request):
    fecha_actual=datetime.datetime.now()
    return render(request,'curso_c.html',{"dame_fecha":fecha_actual})
def curso_css(request):
    fecha_actual=datetime.datetime.now()
    return render(request,'curso_css.html',{"dame_fecha":fecha_actual})

def dame_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>     
        <body>                   
            <h2>
            Fecha y hora actuales: %s
            </h2>
        </body>
    </html>"""%fecha_actual
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")
def calcula_edad(request,edad,anio):
    #edadact=18
    periodo=anio-2023
    edadfut=edad+periodo
    documento="<html><body><h2>EN EL AÑO %s TENDRAS %s AÑOS</body></h2></html>"%(anio,edadfut)
    return HttpResponse(documento)
