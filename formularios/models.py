from django.db import models

# Create your models here.


class Clubes(models.Model):
    nombre = models.CharField(max_length=100)
    presidente = models.CharField(max_length=100)
    vicepresidente = models.CharField(max_length=100)

    class Mate():
        verbose_name_plural = "Clube"

    def __str__(self):
        return self.nombre


class Estadios(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    inauguracion = models.DateField()
    cod_club = models.ForeignKey(Clubes, on_delete=models.CASCADE)

    class Mate():
        verbose_name_plural = "Estadios"

    def __str__(self):
        return self.cod_club


class Trofeos(models.Model):
    nombre = models.CharField(max_length=100)

    class Mate():
        verbose_name_plural = "Trofeos"

    def __str__(self):
        return self.nombre


class palmares(models.Model):
    cod_trofeo = models.ForeignKey(Trofeos, on_delete=models.CASCADE)
    cod_club = models.ForeignKey(Clubes, on_delete=models.CASCADE)
    fecha = models.DateField()

    class Mate():
        verbose_name_plural = "palmarés"

    def __str__(self):
        return f'{self.cod_trofeo} {self.cod_club}'


class Jugadores(models.Model):
    nombre = models.CharField(max_length=100)
    numero_camisa = models.IntegerField()

    class Mate():
        verbose_name_plural = "palmarés"
    def __str__(self):
        return f'{self.nombre} {self.numero_camisa}'



class ClubJug(models.Model):
    cod_club = models.ForeignKey(Clubes, on_delete=models.CASCADE)
    cod_jug = models.ForeignKey(Jugadores, on_delete=models.CASCADE)

    class Mate():
        verbose_name_plural = "integrantes"
        db_table = 'music_album'

    def __str__(self):
        return f'{self.cod_jug} {self.cod_club}'
