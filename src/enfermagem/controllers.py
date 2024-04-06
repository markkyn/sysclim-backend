from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def cadastrar_vacina(request):
    pass

@login_required(login_url="/login/")
def listar_vacinas(request):
    pass