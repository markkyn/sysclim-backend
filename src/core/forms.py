from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model
from common.models import Especialidade

User = get_user_model()

GENERO_CHOICES = (
    (None, "Selecione o Genero"),
    ("M", "Masculino"),
    ("F", "Feminino")
)

CARGO_CHOICES = (
    (None, "Selecione o Cargo"),
    ("médico", "Médico"),
    ("enfermeiro", "Enfermeiro"),
    ("assistente", "Assistente"),
    ("admin", "Administrador")
)


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


class CadastroForm(forms.Form):
        nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'autofocus': True}))
        cpf = forms.CharField(label='CPF', max_length=11, min_length=11)
        genero = forms.ChoiceField(label='Genero', choices=GENERO_CHOICES)
        dt_nascimento = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'type': 'date'}))
        cargo = forms.ChoiceField(label="Cargo",choices=CARGO_CHOICES)
        especialidade = forms.ModelChoiceField(label='Especialidade', queryset=Especialidade.objects.all())
        email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))

        # Endereco
        rua = forms.CharField(label="Rua", max_length=64)
        bairro = forms.CharField(label="Bairro", max_length=64)
        numero = forms.CharField(label="Numero", required=False)
        complemento = forms.CharField(label="Complemento", required=False)
        estado = forms.CharField(label="Estado (Sigla)", max_length=2)
        cidade = forms.CharField(label="Cidade", max_length=24)
        cep = forms.CharField(label="CEP", max_length=8, min_length=8)


class AtualizarForm(forms.Form):
    nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'autofocus': True}))
    cpf = forms.CharField(label='CPF', max_length=11, min_length=11)
    genero = forms.ChoiceField(label='Genero', choices=GENERO_CHOICES)
    dt_nascimento = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(format=['%d-%m-%Y'], attrs={'class': 'form-control', 'type': 'date'}))
    cargo = forms.ChoiceField(label="Cargo", choices=CARGO_CHOICES)
    especialidade = forms.ModelChoiceField(label='Especialidade', queryset=Especialidade.objects.all())
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Senha', strip=False, widget=forms.PasswordInput, required=False)

    # Endereco
    rua = forms.CharField(label="Rua", max_length=64)
    bairro = forms.CharField(label="Bairro", max_length=64)
    numero = forms.CharField(label="Numero", required=False)
    complemento = forms.CharField(label="Complemento", required=False)
    estado = forms.CharField(label="Estado (Sigla)", max_length=2)
    cidade = forms.CharField(label="Cidade", max_length=24)
    cep = forms.CharField(label="CEP", max_length=8, min_length=8)

    def __init__(self, *args, **kwargs):
        super(AtualizarForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['readonly'] = True
