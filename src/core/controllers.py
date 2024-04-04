from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def index(request):
    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            # O framework já realiza a autenticação e validação do formulário
            email = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Redireciona para a página desejada após o login
                return redirect('página_após_login')
            else:
                # Mensagem de erro de autenticação
                login_form.add_error(None, "Email ou senha incorretos.")
    else:
        login_form = LoginForm()

    return render(request, "index.html", locals())