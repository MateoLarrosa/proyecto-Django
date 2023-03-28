from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.mi_vista),
    path('mostrar-fecha/',views.mostrar_fecha),
    #pasando parametros por URL
    path('suma/<int:num1>/<int:num2>/',views.suma),
    path('otro-template/',views.prueba_template),
    path('mi-primer-template/',views.mi_primer_template),
    path('crear-animal/',views.crear_animal),
    path('prueba-render/',views.prueba_render),
]