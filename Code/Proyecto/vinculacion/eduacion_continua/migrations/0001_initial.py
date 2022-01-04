# Generated by Django 4.0 on 2022-01-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(null=True)),
                ('capacidad', models.CharField(max_length=100)),
                ('numeros_de_horas', models.IntegerField(max_length=4)),
            ],
        ),
    ]
