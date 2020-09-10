from django.forms import ModelForm
from .models import Clubes, ClubJug, Jugadores, palmares, Estadios, Trofeos


class ClubesForm(ModelForm):
    class Meta:
        model = Clubes
        fields = '__all__'


class JugadoresForm(ModelForm):
    class Meta:
        model = Jugadores
        fields = '__all__'


class ClubJugForm(ModelForm):
    class Meta:
        model = ClubJug
        fields = '__all__'


class palmaresForm(ModelForm):
    class Meta:
        model = palmares
        fields = '__all__'


class TrofeosForm(ModelForm):
    class Meta:
        model = Trofeos
        fields = '__all__'


class EstadiosForm(ModelForm):
    class Meta:
        model = Estadios
        fields = '__all__'
