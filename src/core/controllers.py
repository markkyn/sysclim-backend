from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

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
    return render(request, "index.html", locals())