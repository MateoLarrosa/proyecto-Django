from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('',views.index,name='index'),
    path('mostrar-fecha/',views.mostrar_fecha,name='mostrar_fecha'),
    #pasando parametros por URL
    path('suma/<int:num1>/<int:num2>/',views.suma,name='suma'),
    path('otro-template/',views.prueba_template,name='otro_template'),
    path('crear-animal/',views.crear_animal,name='crear_animal'),
    path('prueba-render/',views.prueba_render,name='prueba_render'),
    path('familia-mateo/',views.mi_familia,name='familia_mateo'),
    #path('mi-primer-template/',views.mi_primer_template),
]