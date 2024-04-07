# Generated by Django 4.2.11 on 2024-04-05 03:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0006_alter_atestado_dh_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atestado',
            name='dh_criacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 3, 10, 56, 308861)),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='dh_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 3, 10, 56, 308076), verbose_name='Data e Hora de Realização'),
        ),
        migrations.AlterField(
            model_name='exame',
            name='dh_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 3, 10, 56, 308453)),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='dh_criacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 3, 10, 56, 308657)),
        ),
    ]