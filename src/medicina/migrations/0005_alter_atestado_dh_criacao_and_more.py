# Generated by Django 4.2.11 on 2024-04-04 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0004_alter_atestado_dh_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atestado',
            name='dh_criacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 4, 21, 27, 3, 688985)),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='dh_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 4, 21, 27, 3, 688185)),
        ),
        migrations.AlterField(
            model_name='exame',
            name='dh_realizacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 4, 21, 27, 3, 688450)),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='dh_criacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 4, 21, 27, 3, 688777)),
        ),
    ]