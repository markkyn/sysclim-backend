from django import forms

from common.models import Paciente

class CadastroPacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'genero', 'email', 'dt_nascimento']
        widgets = {
            'dt_nascimento': forms.DateTimeInput(attrs={'type': 'datelocal'}, format='%d-%m-%Y'),
        }
    
    def __init__(self, *args, **kwargs):
        super(CadastroPacienteForm, self).__init__(*args, **kwargs)
        self.fields['dh_realizacao'].input_formats = ('%d-%m-%Y',)