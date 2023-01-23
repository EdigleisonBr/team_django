from django.contrib import admin

#Importar as classes
from .models import Atleta, Local, Arbitro, Time, Jogo, Gol


# Register your models here.
admin.site.register(Atleta)
admin.site.register(Local)
admin.site.register(Arbitro)
admin.site.register(Time)
admin.site.register(Jogo)
admin.site.register(Gol)
