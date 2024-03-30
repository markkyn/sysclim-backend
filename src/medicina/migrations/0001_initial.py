# Generated by Django 4.2.11 on 2024-03-30 06:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('crm', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.profissionalsaude')),
            ],
        ),
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dh_criacao', models.DateTimeField(default=datetime.datetime(2024, 3, 30, 6, 24, 31, 950398))),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medicina.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=64)),
                ('dh_realizacao', models.DateTimeField(default=datetime.datetime(2024, 3, 30, 6, 24, 31, 950170))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.assistente')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dh_realizacao', models.DateTimeField(default=datetime.datetime(2024, 3, 30, 6, 24, 31, 949899))),
                ('objetivo', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.assistente')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medicina.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.paciente')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Atestado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dh_criacao', models.DateTimeField(default=datetime.datetime(2024, 3, 30, 6, 24, 31, 950567))),
                ('informacoes', models.TextField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medicina.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.paciente')),
            ],
        ),
    ]
