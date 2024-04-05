from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from common.models import Paciente, Assistente, Endereco, ProfissionalSaude
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
            except:
                endereco.delete()
                form.add_error(None, "Erro ao cadastrar paciente.")

                return redirect("comum:listar_pacientes")
            
    else:
        form = CadastroPacienteForm()

    return render(request, "pacientes/cadastrar_paciente.html", {'form': form})


# PROFISSIONAIS
def listar_profissionais(request):
    profissionais = ProfissionalSaude.objects.all()

    profissionais_count = profissionais.count()

    return render(request, "profissionais/listar_profissionais.html", locals())

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
                    created_by = Assistente.objects.get(id = request.user.identificador_cargo())
                )
            except Exception as e:
                endereco.delete()
                form.add_error(None, f"{str(e)}")
                return render(request, "profissionais/cadastrar_profissional.html", {'form': form})
    else:
        form = CadastroProfissionalForm()

    return render(request, "profissionais/cadastrar_profissional.html", {'form': form})