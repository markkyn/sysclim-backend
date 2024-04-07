from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from common.models import Paciente, Assistente, Endereco, ProfissionalSaude, Sala, Escala
from medicina.models import Especialidade, Medico
from enfermagem.models import Enfermeiro
from common.forms import *

# PACIENTES
@login_required(login_url="/login/")
def listar_pacientes(request):
    pacientes = Paciente.objects.all()

    pacientes_count = pacientes.count()

    return render(request, "pacientes/listar_pacientes.html", locals())

@login_required(login_url="/login/")
def cadastrar_paciente(request):
    if request.method == 'POST':
        form = CadastroPacienteForm(request.POST)
        if form.is_valid():
            endereco_form = {
                # Obrigatorios
                "rua" : form.cleaned_data["rua"],
                "bairro": form.cleaned_data["bairro"],
                "estado": form.cleaned_data["estado"],
                "cidade": form.cleaned_data["cidade"],
                "cep": form.cleaned_data["cep"],
                # Opcionais
                "numero": form.cleaned_data["numero"],
                "complemento": form.cleaned_data["complemento"],
            }
            endereco = Endereco.objects.create(
                rua = endereco_form["rua"],
                bairro = endereco_form["bairro"],
                estado = endereco_form["estado"],
                cidade = endereco_form["cidade"],
                cep = endereco_form["cep"],
                numero = endereco_form["numero"],
                complemento = endereco_form["complemento"]
            )

            try:
                paciente = Paciente.objects.create(
                    endereco = endereco,
                    nome = form.cleaned_data["nome"],
                    cpf = form.cleaned_data["cpf"],
                    genero = form.cleaned_data["genero"],
                    email = form.cleaned_data["email"],
                    dt_nascimento = form.cleaned_data["dt_nascimento"],
                    created_by = Assistente.objects.get(id = request.user.identificador_cargo())
                )
            except Exception as e:
                endereco.delete()
                form.add_error(None, f"Erro ao cadastrar paciente. {str(e)}")
                
                return render(request, "pacientes/cadastrar_paciente.html", {'form': form})

            return redirect("comum:listar_pacientes")
    else:
        form = CadastroPacienteForm()

    return render(request, "pacientes/cadastrar_paciente.html", {'form': form})

# PROFISSIONAIS
@login_required(login_url="/login/")
def listar_profissionais(request):
    profissionais = ProfissionalSaude.objects.all()

    profissionais_count = profissionais.count()

    return render(request, "profissionais/listar_profissionais.html", locals())

@login_required(login_url="/login/")
def cadastrar_profissional(request):
    if request.method == 'POST':
        form = CadastroProfissionalForm(request.POST)
        if form.is_valid():
            endereco_form = {
                # Obrigatorios
                "rua" : form.cleaned_data["rua"],
                "bairro": form.cleaned_data["bairro"],
                "estado": form.cleaned_data["estado"],
                "cidade": form.cleaned_data["cidade"],
                "cep": form.cleaned_data["cep"],
                # Opcionais
                "numero": form.cleaned_data["numero"],
                "complemento": form.cleaned_data["complemento"],
            }
            endereco = Endereco.objects.create(
                rua = endereco_form["rua"],
                bairro = endereco_form["bairro"],
                estado = endereco_form["estado"],
                cidade = endereco_form["cidade"],
                cep = endereco_form["cep"],
                numero = endereco_form["numero"],
                complemento = endereco_form["complemento"]
            )

            try:
                profissional = ProfissionalSaude.objects.create(
                    endereco = endereco,
                    nome = form.cleaned_data["nome"],
                    cpf = form.cleaned_data["cpf"],
                    genero = form.cleaned_data["genero"],
                    email = form.cleaned_data["email"],
                    dt_nascimento = form.cleaned_data["dt_nascimento"],
                    cargo = form.cleaned_data["cargo"],
                    especialidade = form.cleaned_data["especialidade"],
                )

                if form.cleaned_data["cargo"] == "médico":
                    Medico.objects.create(
                        crm = form.cleaned_data["codigo_cargo"],
                        profissional = profissional
                    )
                elif form.cleaned_data["cargo"] == "enfermeiro":
                    Enfermeiro.objects.create(
                        coren = form.cleaned_data["codigo_cargo"],
                        profissional = profissional
                    )   

                return redirect("comum:listar_profissionais")
            except Exception as e:
                endereco.delete()
                form.add_error(None, f"{str(e)}")
                return render(request, "profissionais/cadastrar_profissional.html", {'form': form})
    else:
        form = CadastroProfissionalForm()

    return render(request, "profissionais/cadastrar_profissional.html", {'form': form})

def visualizar_profissional(request, profissional_cpf):
    profissional = get_object_or_404(ProfissionalSaude, cpf=profissional_cpf)
    escalas = Escala.objects.filter(profissionais=profissional)
    if profissional.cargo == "médico":
        cargo = Medico.objects.get(profissional=profissional)
    elif profissional.cargo == "enfermeiro":
        cargo = Enfermeiro.objects.get(profissional=profissional)

    return render(request, "profissionais/visualizar_profissional.html", locals())

# DEPENDENCIAS
@login_required(login_url="/login/")
def listar_salas(request):
    salas = Sala.objects.all()
    salas_count = salas.count()

    return render(request, "dependencias/listar_salas.html", locals())

@login_required(login_url="/login/")
def cadastrar_sala(request):
    if request.method == 'POST':
        form = CadastroSalaForm(request.POST)
        if form.is_valid():
            try:
                sala = Sala.objects.create(
                    numero = form.cleaned_data["numero"],
                )

                return redirect("index")
            except Exception as e:
                form.add_error(None, f"{str(e)}")
                return render(request, "dependencias/cadastrar_sala.html", {'form': form})
    else:
        form = CadastroSalaForm()

    return render(request, "dependencias/cadastrar_sala.html", {'form': form})

# ESPECIALIDADES
@login_required(login_url="/login/")
def cadastrar_especialidade(request):
    if request.method == 'POST':
        form = CadastroEspecialidadeForm(request.POST)
        if form.is_valid():
            try:
                especialidade = Especialidade.objects.create(
                    tuss = form.cleaned_data["tuss"],
                    nome = form.cleaned_data["nome"],
                )

                return redirect("index")
            except Exception as e:
                form.add_error(None, f"{str(e)}")
                return render(request, "especialidades/cadastrar_especialidades.html", {'form': form})
    else:
        form = CadastroEspecialidadeForm()

    return render(request, "especialidades/cadastrar_especialidades.html", {'form': form})

# ESCALAS
@login_required(login_url="/login/")
def listar_escalas(request):
    escalas = Escala.objects.all()
    escalas_count = escalas.count()

    return render(request, "escalas/listar_escalas.html", locals())

@login_required(login_url="/login/")
def cadastrar_escala(request):
    if request.method == 'POST':
        form = CadastroEscalaForm(request.POST)
        if form.is_valid():
            try:
                escala = Escala.objects.create(
                    dt_inicio = form.cleaned_data["data_inicio"],
                    dt_final = form.cleaned_data["data_final"],
                    hr_inicio = form.cleaned_data["hora_inicio"],
                    hr_final = form.cleaned_data["hora_final"],
                )

                return redirect("index")
            except Exception as e:
                form.add_error(None, f"{str(e)}")
                return render(request, "escalas/cadastrar_escala.html", {'form': form})
    else:
        form = CadastroEscalaForm()

    return render(request, "escalas/cadastrar_escala.html", {'form': form})

@login_required(login_url="/login/")
def aplicar_escala(request, escala_id):
    escala = Escala.objects.get(id=escala_id)
    profissionais_ids = escala.profissionais.all().values_list('cpf', flat=True)
    if request.method == 'POST':
        form = AplicarEscalaForm(request.POST)
        if form.is_valid():
            try:
                profissionais = form.cleaned_data["profissionais"]
                escala.profissionais.set(profissionais)

                return redirect("index")

            except Exception as e:
                form.add_error(None, f"{str(e)}")
                return render(request, "escalas/aplicar_escala.html", {'form': form})
    else:
        form = AplicarEscalaForm(
            initial={
                "profissionais": escala.profissionais.all().values_list('cpf', flat=True)
            }
        )

    return render(request, "escalas/aplicar_escala.html", {'form': form})