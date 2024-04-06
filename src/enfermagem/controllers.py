from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from enfermagem.models import Vacina

from enfermagem.forms import CadastroVacinaForm


@login_required(login_url="/login/")
def cadastrar_vacina(request):
    if request.method == "POST":
        form = CadastroVacinaForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data.get("nome")
            descricao = form.cleaned_data.get("descricao")
            data_fabricacao = form.cleaned_data.get("data_fabricacao")
            data_validade = form.cleaned_data.get("data_validade")

            vacina = Vacina.objects.create(
                nome=nome,
                descricao=descricao,
                data_fabricacao=data_fabricacao,
                data_validade=data_validade,
                paciente = None,
                enfermeiro = None
            )
            
            return redirect("enfermeiro:listar_vacinas")

        else:
            form.add_error(None, "Erro ao cadastrar vacina.")

    else:
        form = CadastroVacinaForm()

    return render(request, "vacinas/cadastrar_vacina.html", locals())


@login_required(login_url="/login/")
def listar_vacinas(request):
    vacinas = Vacina.objects.all()
    vacinas_count = vacinas.count()

    return render(request, "vacinas/listar_vacinas.html", locals())