"""checker_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from formularios.views import index, jugadores, club, clubJugadores, trofeos, estadio, palmares
from formularios.views import lis_jugador, del_jugador, act_jugador

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('jugador', jugadores, name='jugador'),
    path('club', club, name='club'),
    path('jugador-club', clubJugadores, name='jugador-club'),
    path('estadio/', estadio, name='estadio'),
    path('trofeos', trofeos, name='trofeos'),
    path('palmares', palmares, name='palmares'),
    path('jugadores-lista/', lis_jugador, name='list-jugador'),
    path('borrar-jugadores/<int:id>/', del_jugador, name='del-jugador'),
    path('actualizar-jugadores/<int:id>/', act_jugador, name='act-jugador'),
]
