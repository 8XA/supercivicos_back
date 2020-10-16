# Generated by Django 3.1.2 on 2020-10-15 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('empresa', models.CharField(max_length=100, verbose_name='Empresa')),
                ('responsable', models.CharField(max_length=100, verbose_name='Responsable')),
                ('calle', models.CharField(max_length=100, verbose_name='Calle')),
                ('num_exterior', models.CharField(max_length=10, verbose_name='Número exterior')),
                ('num_interior', models.CharField(max_length=10, verbose_name='Número interior')),
                ('colonia', models.CharField(max_length=100, verbose_name='Colonia')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('pais', models.CharField(max_length=100, verbose_name='Pais')),
                ('CP', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('telefono', models.IntegerField(null=True)),
                ('contrasena', models.CharField(max_length=100, verbose_name='Contraseña')),
            ],
        ),
    ]