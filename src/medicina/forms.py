from django import forms

from medicina.models import Consulta, Exame


class CadastroConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'sala', 'dh_realizacao', 'objetivo', ]
        widgets = {
            'dh_realizacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'objetivo': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    def __init__(self, *args, **kwargs):
        super(CadastroConsultaForm, self).__init__(*args, **kwargs)
        self.fields['dh_realizacao'].input_formats = ('%Y-%m-%dT%H:%M',)


class ReagendamentoConsultaForm(forms.Form):
    novo_horario = forms.DateTimeField(label="Novo Horario",
                                       widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))


class EmitirAtestadoForm(forms.Form):
    informacoes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))


'''class CadastroTipoExameForm(forms.Form):
    tipo = forms.CharField(label="Tipo de Exame", max_length=64)'''


class CadastroExameForm(forms.ModelForm):
        class Meta:
            model = Exame
            fields = ['tipo', 'dh_realizacao', 'medico', 'paciente', ]
            widgets = {
                'dh_realizacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            }

        def __init__(self, *args, **kwargs):
            super(CadastroExameForm, self).__init__(*args, **kwargs)
            self.fields['dh_realizacao'].input_formats = ('%Y-%m-%dT%H:%M',)


class ReagendamentoExameForm(forms.Form):
    novo_horario = forms.DateTimeField(label="Novo Horario",
                                       widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))