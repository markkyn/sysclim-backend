from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from medicina.models import Medico , Consulta
from common.models import Paciente, Assistente, Sala

from .forms import CadastroConsultaForm, ReagendamentoConsultaForm

@login_required(login_url="/login/")
def listar_consultas(request):
    consultas = Consulta.objects.all()

    consultas_count = consultas.count()

    return render(request, "listar_consultas.html", locals())

@login_required(login_url="/login/")
def agendar_consulta(request):
    if request.method == 'POST':
        form = CadastroConsultaForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            crm = form.cleaned_data['crm']
            dh_realizacao = form.cleaned_data['dh_realizacao']
            sala_id = form.cleaned_data['sala']
            assistente_id = request.user.assistente.id

            paciente = get_object_or_404(Paciente, cpf=cpf)
            medico = get_object_or_404(Medico, crm=crm)
            sala = get_object_or_404(Sala, id=sala_id)
            assistente = get_object_or_404(Assistente, id=assistente_id)

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

    return render(request, "nova_consulta.html", locals())

@login_required(login_url="/login/")
def cancelar_consulta(request, id):
    consulta = Consulta.objects.get(id = id).delete()

    return redirect("index")

@login_required(login_url="/login/")
def reagendar_consulta(request, id):
    if request.method == 'POST':
        form = ReagendamentoConsultaForm()

        if form.is_valid():
            consulta_antiga = Consulta.objects.get(id = id)
            novo_horario = form.cleaned_data["novo_horario"]

            if consulta_antiga.medico.verificar_disponibilidade(novo_horario):
                # Disponivel
                consulta_antiga.setNovoHorario(novo_horario)

            else:
                # Indisponivel
                # Mensagem de Erro
                pass

    else:
        form = ReagendamentoConsultaForm()
    
    return render(request, "consultas/reagendamento_consulta.html")


