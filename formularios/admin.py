from django.contrib import admin
from .models import Clubes, ClubJug, Jugadores, palmares, Estadios, Trofeos

# Register your models here.
modelos= [Clubes, ClubJug, Jugadores, palmares, Estadios, Trofeos]
for i in modelos:
    admin.site.register(i)