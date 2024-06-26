from django import forms

from enfermagem.models import *

class CadastroVacinaForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=64)
    lote = forms.CharField(label="Lote", max_length=24)
    data_fabricacao = forms.DateField(label="Data de Fabricação",
                                      widget=forms.DateInput(attrs={'type': 'date'}))
    data_validade = forms.DateField(label="Data de Validade",
                                    widget=forms.DateInput(attrs={'type': 'date'}))
    descricao = forms.CharField(label="Descrição", widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

class AplicarVacinaForm(forms.Form):
    VACINAS_CHOICES = Vacina.filtrarAplicaveis().values_list('id', 'nome')

    vacina = forms.ChoiceField(label="Vacina", choices=VACINAS_CHOICES)