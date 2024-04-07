# Generated by Django 4.2.11 on 2024-04-06 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0013_alter_atestado_dh_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atestado',
            name='dh_criacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 6, 1, 34, 38, 267156)),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='dh_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 6, 1, 34, 38, 266463), verbose_name='Data e Hora de Realização'),
        ),
        migrations.AlterField(
            model_name='exame',
            name='dh_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 6, 1, 34, 38, 266754)),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='dh_criacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 6, 1, 34, 38, 266976)),
        ),
    ]