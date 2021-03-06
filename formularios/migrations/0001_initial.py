# Generated by Django 3.0.8 on 2020-09-06 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clubes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('presidente', models.CharField(max_length=100)),
                ('vicepresidente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('numero_camisa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trofeos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='palmares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cod_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularios.Clubes')),
                ('cod_trofeo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularios.Trofeos')),
            ],
        ),
        migrations.CreateModel(
            name='Estadios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('capacidad', models.IntegerField()),
                ('inauguracion', models.DateField()),
                ('cod_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularios.Clubes')),
            ],
        ),
        migrations.CreateModel(
            name='ClubJug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularios.Clubes')),
                ('cod_jug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularios.Jugadores')),
            ],
        ),
    ]
