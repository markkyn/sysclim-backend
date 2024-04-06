from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime


from medicina.models import Medico , Consulta, Atestado
from common.models import Paciente, Assistente, Sala

from .forms import CadastroConsultaForm, ReagendamentoConsultaForm, EmitirAtestadoForm

@login_required(login_url="/login/")
def listar_consultas(request):
    consultas = Consulta.objects.all()

    consultas_count = consultas.count()

    return render(request, "consultas/listar_consultas.html", locals())

@login_required(login_url="/login/")
def agendar_consulta(request):
    if request.method == 'POST':
        form = CadastroConsultaForm(request.POST)
        if form.is_valid():
            medico = Medico.objects.get(crm=form.cleaned_data['medico'].crm)
            paciente = Paciente.objects.get(cpf=form.cleaned_data['paciente'].cpf)

            dh_realizacao = form.cleaned_data['dh_realizacao']
            sala_numero = form.cleaned_data['sala'].numero
            profissional = request.user

            sala = Sala.objects.get(numero = sala_numero)
            assistente = get_object_or_404(Assistente, profissional=profissional)

            if medico.verificar_disponibilidade(dh_realizacao):
                consulta = Consulta.objects.create(
                    dh_realizacao=dh_realizacao,
                    objetivo=form.cleaned_data['objetivo'],
                    paciente=paciente,
                    medico=medico,
                    sala=sala,
                    created_by=assistente
                )
                return redirect("index")
            else:
                form.add_error(None, "Médico não disponível para esta data/horário.")
    else:
        form = CadastroConsultaForm()

    return render(request, "consultas/nova_consulta.html", locals())

@login_required(login_url="/login/")
def cancelar_consulta(request, id):
    consulta = Consulta.objects.get(id = id).delete()

    return redirect("index")

@login_required(login_url="/login/")
def reagendar_consulta(request,id):
    if request.method == 'POST':
        form = ReagendamentoConsultaForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ReagendamentoConsultaForm()

    return render(request, "consultas/reagendamento_consulta.html", locals())

@login_required(login_url="/login/")
def realizar_consulta(request, id):
    consulta = Consulta.objects.get(id = id)

    return render(request, "consultas/realizar_consulta.html", locals())

@login_required(login_url="/login/")
def finalizar_consulta(request, id):
    consulta = Consulta.objects.get(id = id)
    consulta.status = 'realizada'
    consulta.save()

    return redirect("index")

@login_required(login_url="/login/")
def emitir_atestado(request, id):
    consulta = Consulta.objects.get(id = id)
    
    if request.method == 'POST':
        form = EmitirAtestadoForm(request.POST)
    
        if form.is_valid():
            
            Atestado.objects.create(
                medico = consulta.medico,
                paciente = consulta.paciente,
                informacoes = form.cleaned_data['informacoes'],
                dh_criacao = datetime.now(),
            )

            redirect("realizar_consulta", id=id)

    else:
        form = EmitirAtestadoForm()

    return render(request, "atestados/novo_atestado.html", locals())