from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, CadastroForm, AtualizarForm
from common.models import *
from medicina.models import *

import sweetify


def login_ctrl(request):
    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if password == 'abcd1234':
                    sweetify.warning(request, 'Por favor, altere sua senha!')
                    return redirect('visualizar_perfil', usuario_cpf=user.cpf)
                return redirect('index')
            else:
                login_form.add_error(None, "Email ou senha incorretos.")
    else:
        login_form = LoginForm()

    return render(request, "login.html", locals())


@login_required(login_url="/login/")
def logout_ctrl(request):
    logout(request)
    return redirect('login')


@login_required(login_url="/login/")
def cadastro_usuario_ctrl(request):
    if request.method == "POST":
        cadastro_form = CadastroForm(request.POST)
        if cadastro_form.is_valid():
            print(cadastro_form.cleaned_data)
            endereco_form = {
                # Obrigatorios
                "rua": cadastro_form.cleaned_data["rua"],
                "bairro": cadastro_form.cleaned_data["bairro"],
                "estado": cadastro_form.cleaned_data["estado"],
                "cidade": cadastro_form.cleaned_data["cidade"],
                "cep": cadastro_form.cleaned_data["cep"],
                # Opcionais
                "numero": cadastro_form.cleaned_data["numero"],
                "complemento": cadastro_form.cleaned_data["complemento"],
            }
            endereco = Endereco.objects.create(
                rua=endereco_form["rua"],
                bairro=endereco_form["bairro"],
                estado=endereco_form["estado"],
                cidade=endereco_form["cidade"],
                cep=endereco_form["cep"],
                numero=endereco_form["numero"],
                complemento=endereco_form["complemento"]
            )
            print("ENDERECO CRIADO")
            try:
                print('funcao')
                manager = get_user_model()
                user = manager(
                    email=cadastro_form.cleaned_data["email"],
                    cpf=cadastro_form.cleaned_data["cpf"],
                    nome=cadastro_form.cleaned_data["nome"],
                    genero=cadastro_form.cleaned_data["genero"],
                    dt_nascimento=cadastro_form.cleaned_data["dt_nascimento"],
                    cargo=cadastro_form.cleaned_data["cargo"],
                    especialidade_id=cadastro_form.cleaned_data["especialidade"],
                    endereco_id=endereco.id,
                    is_active=True,
                    is_staff=False,
                )
                user.set_password("abcd1234")
                user.save()
                print("USUARIO CRIADO")
                sweetify.success(request, 'Usuário criado com sucesso!')
            except Exception as e:
                endereco.delete()
                cadastro_form.add_error(None, f"Erro ao cadastrar usuário. {str(e)}")
                sweetify.error(request, 'Erro ao cadastrar usuário!')
            return render(request, "cadastro.html", {'form': cadastro_form})
    else:
        cadastro_form = CadastroForm()
    return render(request, "cadastro.html", {'form': cadastro_form})


@login_required(login_url="/login/")
def delete_usuario_ctrl(request, usuario_cpf):
    try:
        user = get_user_model().objects.get(cpf=usuario_cpf)
        user.delete()
        sweetify.success(request, 'Usuário deletado com sucesso!')
    except Exception as e:
        sweetify.error(request, 'Erro ao deletar usuário!')
    return redirect('visualizar_usuarios')


@login_required(login_url="/login/")
def visualizar_perfil_ctrl(request, usuario_cpf):
    if request.method == "POST":
        visualizar_form = AtualizarForm(request.POST)

        if visualizar_form.is_valid():
            endereco_form = {
                # Obrigatorios
                "rua": visualizar_form.cleaned_data["rua"],
                "bairro": visualizar_form.cleaned_data["bairro"],
                "estado": visualizar_form.cleaned_data["estado"],
                "cidade": visualizar_form.cleaned_data["cidade"],
                "cep": visualizar_form.cleaned_data["cep"],
                # Opcionais
                "numero": visualizar_form.cleaned_data["numero"],
                "complemento": visualizar_form.cleaned_data["complemento"],
            }
            endereco = Endereco.objects.create(
                rua=endereco_form["rua"],
                bairro=endereco_form["bairro"],
                estado=endereco_form["estado"],
                cidade=endereco_form["cidade"],
                cep=endereco_form["cep"],
                numero=endereco_form["numero"],
                complemento=endereco_form["complemento"]
            )
            user = get_user_model().objects.get(cpf=usuario_cpf)
            try:
                user.cpf = visualizar_form.cleaned_data["cpf"]
                user.email = visualizar_form.cleaned_data["email"]
                user.nome = visualizar_form.cleaned_data["nome"]
                user.genero = visualizar_form.cleaned_data["genero"]
                user.dt_nascimento = visualizar_form.cleaned_data["dt_nascimento"]
                user.cargo = visualizar_form.cleaned_data["cargo"]
                user.especialidade_id = visualizar_form.cleaned_data["especialidade"]
                user.endereco_id = endereco.id
                if visualizar_form.cleaned_data["password"]:
                    user.set_password(visualizar_form.cleaned_data["password"])
                user.save()
            except Exception as e:
                endereco.delete()
                visualizar_form.add_error(None, f"Erro ao atualizar usuário. {str(e)}")
                sweetify.error(request, 'Erro ao atualizar usuário!')
                return render(request, "visualizar_perfil.html", {'form': visualizar_form})
            sweetify.success(request, 'Usuario atualizado com sucesso!')
            return redirect('visualizar_usuarios')
        else:
            sweetify.error(request, 'Erro ao atualizar usuário!')
            return render(request, "visualizar_perfil.html", {'form': visualizar_form})
        return redirect('visualizar_usuarios')
    else:
        user = get_user_model().objects.get(cpf=usuario_cpf)
        endereco = user.endereco
        dt_nascimento = user.dt_nascimento.strftime('%d/%m/%Y')
        visualizar_form = AtualizarForm(
            initial={
                "email": user.email,
                "cpf": user.cpf,
                "nome": user.nome,
                "genero": user.genero,
                "password": user.password,
                "dt_nascimento": dt_nascimento,
                "cargo": user.cargo,
                "especialidade": user.especialidade_id,
                "rua": endereco.rua,
                "bairro": endereco.bairro,
                "numero": endereco.numero,
                "complemento": endereco.complemento,
                "estado": endereco.estado,
                "cidade": endereco.cidade,
                "cep": endereco.cep,
            }
        )
    return render(request, "visualizar_perfil.html", {'form': visualizar_form})


@login_required(login_url="/login/")
def reset_password_ctrl(request, usuario_cpf):
    try:
        user = get_user_model().objects.get(cpf=usuario_cpf)
        user.set_password("abcd1234")
        user.save()
        sweetify.success(request, 'Senha resetada com sucesso!')
        return redirect('visualizar_usuarios')
    except Exception as e:
        sweetify.error(request, 'Erro ao resetar senha!')
        return redirect('visualizar_usuarios')


@login_required(login_url="/login/")
def visualizar_usuarios_ctrl(request):
    #Apenas usuarios que tenham password
    usuarios = ProfissionalSaude.objects.all(
    ).exclude(
        email__isnull=True
    ).exclude(
        email__exact=''
    ).exclude(
        password__isnull=True
    ).exclude(
        password__exact=''
    )
    return render(request, "visualizar_usuarios.html", locals())


@login_required(login_url="/login/")
def index(request):
    consultas_count = Consulta.objects.all().count()
    pacientes_count = Paciente.objects.all().count()
    exames_count = Exame.objects.all().count()
    profissional_count = ProfissionalSaude.objects.all().count()
    salas_count = Sala.objects.all().count()

    return render(request, "base/index.html", locals())
