from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from common.models import *
from medicina.models import *

def login_ctrl(request):
    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                login_form.add_error(None, "Email ou senha incorretos.")
    else:
        login_form = LoginForm()

    return render(request, "login.html", locals())

@login_required(login_url="/login/")
def index(request):
    consultas_count = Consulta.objects.all().count()
    pacientes_count = Paciente.objects.all().count()
    exames_count = Exame.objects.all().count()
    profissional_count = ProfissionalSaude.objects.all().count()

    return render(request, "base/index.html", locals())
