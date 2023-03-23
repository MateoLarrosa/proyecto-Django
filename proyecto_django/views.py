from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context

def mi_vista(request):
    return HttpResponse('<h1>Mi primera vista</h1><br><p>soy un parrafo</p>')

def mostar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime('%A %d %B %Y %I:%M')
    return HttpResponse(f'<p>{dt_formateado}</p>')

def saludar(request,num1,num2):
    if type(num1) == int and type(num2) == int:
        rta = num1 + num2
        return HttpResponse(f'<p> El resultado de {num1} + {num2} es {rta}</p>') 
    else:
       return HttpResponse('<p>Solo puedo sumar numeros</p>')

def mi_primer_template(request):
    archivo = open(r'C:\Users\Usuario\Desktop\clase17\proyecto-Django\templates\mi_template.html','r')
    
    template = Template(archivo.read())
    
    archivo.close()
    
    context = Context()
    
    template_renderizado = template.render(context)
    
    return HttpResponse(template_renderizado)
