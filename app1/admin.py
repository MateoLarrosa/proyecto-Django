from django.contrib import admin
from app1.models import Animal,Familiares
# Register your models here.

admin.site.register([Animal,Familiares])