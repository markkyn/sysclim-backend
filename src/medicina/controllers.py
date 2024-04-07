from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime

from medicina.models import Medico, Consulta, Atestado, Prontuario, Exame
from common.models import Paciente, Assistente, Sala

from .forms import CadastroConsultaForm, ReagendamentoConsultaForm, EmitirAtestadoForm, CadastroExameForm, \
    ReagendamentoExameForm


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

            sala = Sala.objects.get(numero=sala_numero)
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
    consulta = Consulta.objects.get(id=id)
    consulta.status = 'cancelada'
    consulta.save()

    return redirect("medicina:listar_consultas")


@login_required(login_url="/login/")
def reagendar_consulta(request, id):
    if request.method == 'POST':
        form = ReagendamentoConsultaForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ReagendamentoConsultaForm()

    return render(request, "consultas/reagendamento_consulta.html", locals())


@login_required(login_url="/login/")
def realizar_consulta(request, id):
    consulta = Consulta.objects.get(id=id)

    return render(request, "consultas/realizar_consulta.html", locals())


@login_required(login_url="/login/")
def finalizar_consulta(request, id):
    consulta = Consulta.objects.get(id=id)
    consulta.status = 'realizada'
    consulta.save()

    return redirect("index")


@login_required(login_url="/login/")
def emitir_atestado(request, id):
    consulta = Consulta.objects.get(id=id)

    if request.method == 'POST':
        form = EmitirAtestadoForm(request.POST)

        if form.is_valid():
            Atestado.objects.create(
                medico=consulta.medico,
                paciente=consulta.paciente,
                informacoes=form.cleaned_data['informacoes'],
                dh_criacao=datetime.now(),
            )

            redirect("medicina:realizar_consulta", id=id)

    else:
        form = EmitirAtestadoForm()

    return render(request, "atestados/novo_atestado.html", locals())


# PRONTUARIO
@login_required(login_url="/login/")
def visualizar_prontuario(request, paciente_cpf):
    paciente = Paciente.objects.get(cpf=paciente_cpf)

    try:
        prontuario = Prontuario.objects.get(paciente=paciente)

    except Prontuario.DoesNotExist:
        prontuario = Prontuario.objects.create(
            paciente=paciente,
        )

    atestados = prontuario.getAtestados()
    vacinas = prontuario.getVacinasAplicadas()

    return render(request, "prontuarios/visualizar_prontuario.html", locals())


# EXAMES
@login_required(login_url="/login/")
def listar_exames(request):
    exames = Exame.objects.all()

    exames_count = exames.count()

    return render(request, "exames/listar_exames.html", locals())


@login_required(login_url="/login/")
def agendar_exame(request):
    if request.method == 'POST':
        form = CadastroExameForm(request.POST)
        if form.is_valid():
            medico = Medico.objects.get(crm=form.cleaned_data['medico'].crm)
            paciente = Paciente.objects.get(cpf=form.cleaned_data['paciente'].cpf)

            dh_realizacao = form.cleaned_data['dh_realizacao']
            tipo = form.cleaned_data['tipo']
            profissional = request.user
            assistente = get_object_or_404(Assistente, profissional=profissional)

            if medico.verificar_disponibilidade(dh_realizacao):
                exame = Exame.objects.create(
                    tipo=tipo,
                    dh_realizacao=dh_realizacao,
                    paciente=paciente,
                    medico=medico,
                    created_by=assistente
                )
                return redirect("index")
            else:
                form.add_error(None, "Médico não disponível para esta data/horário.")
    else:
        form = CadastroExameForm()

    return render(request, "exames/novo_exame.html", locals())


@login_required(login_url="/login/")
def reagendar_exame(request, id):
    if request.method == 'POST':
        form = ReagendamentoExameForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ReagendamentoExameForm()

    return render(request, "exames/reagendamento_exame.html", locals())
