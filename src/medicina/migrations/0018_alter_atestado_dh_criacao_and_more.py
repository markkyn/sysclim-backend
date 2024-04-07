# Generated by Django 4.2.11 on 2024-04-07 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0017_remove_prontuario_atestados_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atestado',
            name='dh_criacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 0, 41, 7, 805781)),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='dh_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 0, 41, 7, 804775), verbose_name='Data e Hora de Realização'),
        ),
        migrations.AlterField(
            model_name='exame',
            name='dh_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 0, 41, 7, 805033)),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='dh_criacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 0, 41, 7, 805613)),
        ),
    ]
