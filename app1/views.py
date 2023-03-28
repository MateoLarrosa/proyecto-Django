
from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context,loader
from app1.models import Animal

#primera view de la forma mas principiante
def mi_vista(request):
    return HttpResponse('<h1>Mi primera vista</h1><br><p>soy un parrafo</p>')

# view de la forma correcta 
def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime('%A %d %B %Y %I:%M')
    template = loader.get_template('mostrar_fecha.html')
    
    datos = {'fecha': dt_formateado}
    
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)


# view de la forma correcta con parametros por la url
def suma(request,num1,num2):
    Template = loader.get_template('suma.html')
    
    numeros = {
        'num1' : num1,
        'num2' : num2,
        'rta' : num1 + num2
        }
    Template_renderizado = Template.render(numeros)
    return HttpResponse(Template_renderizado)

# template de la forma con el open
def mi_primer_template(request):
    archivo = open(r'C:\Users\Usuario\Desktop\clase17\proyecto-Django\templates\mi_template.html','r')
    
    template = Template(archivo.read())
    
    archivo.close()
    
    context = Context(template)
    
    template_renderizado = template.render(context)
    
    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    datos = {
        'nombre': 'Pepito',
        'apellido': 'Grillo',
        'edad': 14,
        'anios': [
            1995, 2004, 2014, 2017, 2021, 2022
        ]
    }
    
    template = loader.get_template(r'otro_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)

def crear_animal(request):
    animal1 = Animal(nombre='Elias gomez',edad=28)
    animal1.save() #Con este metodo se guarda en la base de datos
    datos = {'animal':animal1} 
    template = loader.get_template(r'crear_animal.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)