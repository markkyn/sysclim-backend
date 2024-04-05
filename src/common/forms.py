from django import forms

from common.models import Paciente, Especialidade

GENERO_CHOICES = (
    (None, "Selecione o Genero"),
    ("M", "Masculino"),
    ("F", "Feminino")
)

CARGO_CHOICES = (
    (None, "Selecione o Cargo"),
    ("médico", "Médico"),
    ("enfermeiro", "Enfermeiro"),
    ("assistente", "Assistente")
)


class CadastroPacienteForm(forms.Form):
    nome = forms.CharField(label="Nome")
    cpf = forms.CharField(label="CPF",max_length=11, min_length=11)
    genero = forms.ChoiceField(label="Genero",choices=GENERO_CHOICES)
    email = forms.EmailField(label="Email")
    dt_nascimento = forms.DateField(
        label="Data de Nascimento", 
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                "class": "form-control",
                "type": "date"
            })
        )
    
    # Endereco
    rua = forms.CharField(label="Rua", max_length=64)
    bairro = forms.CharField(label="Bairro", max_length=64)
    numero = forms.CharField(label="Numero", required=False)
    complemento = forms.CharField(label="Complemento", required=False)
    estado = forms.CharField(label="Estado (Sigla)", max_length=2)
    cidade = forms.CharField(label="Cidade", max_length=24)
    cep = forms.CharField(label="CEP", max_length=8, min_length=8)


class CadastroProfissionalForm(forms.Form):
    nome = forms.CharField(label="Nome")
    cpf = forms.CharField(label="CPF",max_length=11, min_length=11)
    genero = forms.ChoiceField(label="Genero",choices=GENERO_CHOICES)
    email = forms.EmailField(label="Email")
    cargo = forms.ChoiceField(label="Cargo",choices=CARGO_CHOICES)
    especialidade = forms.ModelChoiceField(label="Especialidade",queryset=Especialidade.objects.all())
    dt_nascimento = forms.DateField(
        label="Data de Nascimento", 
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                "class": "form-control",
                "type": "date"
            })
        )
    
    # Endereco
    rua = forms.CharField(label="Rua", max_length=64)
    bairro = forms.CharField(label="Bairro", max_length=64)
    numero = forms.CharField(label="Numero", required=False)
    complemento = forms.CharField(label="Complemento", required=False)
    estado = forms.CharField(label="Estado (Sigla)", max_length=2)
    cidade = forms.CharField(label="Cidade", max_length=24)
    cep = forms.CharField(label="CEP", max_length=8, min_length=8)