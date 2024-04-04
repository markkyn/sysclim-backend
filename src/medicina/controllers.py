from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from common.models import Paciente
from .models import Medico , Consulta

@login_required
def listar_consultas(request):
    consultas = Consulta.objects.all()

    consultas_count = consultas.count()

    return render(request, "listar_consultas.html", locals())



@login_required
def agender_consulta(request):
    
    # Busca Paciente por CPF


    Paciente.objects.get(cpf = request.cpf)

    Medico.objects.get(crm = request.crm)