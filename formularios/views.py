from django.shortcuts import render, redirect
# from django.views.generic import TemplateView, CreateView
from .forms import JugadoresForm, ClubesForm, ClubJugForm, palmaresForm, TrofeosForm, EstadiosForm
from .models import Jugadores

# Create your views here.


def index(request):
    return render(request, 'index.html')


def jugadores(request):
    if request.method == 'POST':
        form = JugadoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = JugadoresForm()
    return render(request, 'formularios/jugador.html', {'form': form})


def club(request):
    if request.method == 'POST':
        form = ClubesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClubesForm()
    return render(request, 'formularios/club.html', {'form': form})


def clubJugadores(request):
    if request.method == 'POST':
        form = ClubJugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClubJugForm()
    return render(request, 'formularios/club-jugadores.html', {'form': form})


def palmares(request):
    if request.method == 'POST':
        form = palmaresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = palmaresForm()
    return render(request, 'formularios/palmares.html', {'form': form})


def trofeos(request):
    if request.method == 'POST':
        form = TrofeosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TrofeosForm()
    return render(request, 'formularios/palmares.html', {'form': form})


def estadio(request):
    if request.method == 'POST':
        form = EstadiosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EstadiosForm()
    return render(request, 'formularios/estadio.html', {'form': form})

####################################################################################################

def lis_jugador(request):
    lista = Jugadores.objects.all()
    contexto = {'jugadores': lista}
    return render(request, 'list-formulario/jugador.html', contexto)

def act_jugador(request, id):
    jugador = Jugadores.objects.get(id=id)
    if request.method == 'GET':
        form = JugadoresForm(instance=jugador)
    else:
        form = JugadoresForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
        return redirect('list-jugador')
    return render(request, 'act-formulario/jugador.html',{'form':form})

def del_jugador(request, id):
    jugador = Jugadores.objects.get(id=id)
    if request.method == 'POST':
        jugador.delete()
        return redirect('list-jugador')

    return render(request, 'eliminar/jugador.html',{'jugador':jugador})