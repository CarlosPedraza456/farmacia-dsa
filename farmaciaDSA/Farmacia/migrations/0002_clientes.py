# Generated by Django 4.2.1 on 2023-07-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmacia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_name', models.CharField(max_length=35)),
                ('cliente_apellido', models.CharField(max_length=35)),
                ('cliente_telefono', models.CharField(max_length=35)),
                ('cliente_correo', models.CharField(max_length=35)),
                ('cliente_cedula', models.CharField(max_length=15)),
                ('cliente_fecha', models.DateField()),
            ],
        ),
    ]