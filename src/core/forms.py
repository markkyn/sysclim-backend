from django import forms
from django.forms import PasswordInput
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Senha', strip=False, widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        """
        Inicializa o formulário com o campo de usuário padrão escondido.
        """
        super(LoginForm, self).__init__(request=request, *args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        
        self.fields = {
            'email': self.fields['email'],
            'password': self.fields['password'],
        }

    def clean(self):
        """
        Substitui o valor do campo username com o valor do campo email para autenticação.
        """
        email = self.cleaned_data.get('email')
        if email:
            self.cleaned_data['username'] = email
        return super().clean()