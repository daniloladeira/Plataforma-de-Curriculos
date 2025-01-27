from django import forms
from .models import Curriculo

class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = ['primeironome', 'ultimonome', 'email', 'telefone', 'escolaridade', 'cargodesejado', 'observacoes', 'curriculo']
        widgets = {
            'escolaridade': forms.RadioSelect,
            'primeironome': forms.TextInput(attrs={'placeholder': 'Primeiro Nome'}),
            'ultimonome': forms.TextInput(attrs={'placeholder': 'Último Nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'exemplo@gmail.com'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
            'cargodesejado': forms.TextInput(attrs={'placeholder': 'Desenvolvedor, Administração ...'}),
            'observacoes': forms.Textarea(attrs={'placeholder': 'Observações'}),
            'curriculo': forms.ClearableFileInput(attrs={'placeholder': 'Carregar o Currículo'})
        }