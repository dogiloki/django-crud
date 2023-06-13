from django.http import HttpResponse
import datetime;
from django.template import Template, Context

class Persona(object):

	def __init__(self,nombre,apellido):
		self.nombre=nombre
		self.apellido=apellido

def saludo(req):
	fecha_actual=datetime.datetime.now()
	persona=Persona("Julio","Villanueva")
	doc_externo=open("E:/Github/django/django-crud/app/templates/index.html")
	template=Template(doc_externo.read());
	doc_externo.close();
	temas=[
		"Plantillas",
		"Modelos",
		"Formularios",
		"Vistas"
	]
	ctx=Context({
		"fecha_actual":fecha_actual,
		"persona":persona,
		"temas":temas
	})
	documento=template.render(ctx)
	return HttpResponse(documento)

def calcularEdad(req,year,age):
	periodo=year-2023;
	edad_futura=age+periodo
	documento="""
		<h1>En el año %s tendrás %s años:</h1>
	"""%(year,edad_futura)
	return HttpResponse(documento)