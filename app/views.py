from django.http import HttpResponse

def saludo(req):
	return HttpResponse("Hola alumnos")