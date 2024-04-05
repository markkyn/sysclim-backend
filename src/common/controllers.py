from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from common.models import Paciente
from common.forms import *



@login_required
def listar_pacientes(request):
    pacientes = Paciente.objects.all()

    pacientes_count = pacientes.count()

    return render(request, "pacientes/listar_pacientes.html", locals())


@login_required
def cadastrar_paciente(request):
    if request.method == 'POST':
        form = CadastroPacienteForm(request.POST)
        if form.is_valid():
            novo_paciente = form.save(commit=False)
            novo_paciente.created_by = request.user.assistente
            novo_paciente.save()
            return redirect("index")
    else:
        form = CadastroPacienteForm()

    return render(request, "cadastrar_paciente.html", {'form': form})