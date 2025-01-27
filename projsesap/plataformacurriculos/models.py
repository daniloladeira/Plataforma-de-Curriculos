from django.db import models
from django import forms
from django.core.exceptions import ValidationError

# Modelo
class Curriculo(models.Model):
    primeironome = models.CharField(max_length=100, verbose_name="Primeiro Nome", null=False, blank=False)
    ultimonome = models.CharField(max_length=100, verbose_name="Último Nome", null=False, blank=False)
    email = models.EmailField(max_length=100, verbose_name="E-Mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cargodesejado = models.CharField(max_length=100, verbose_name="Posição Desejada")
    
    OPCOES_ESCOLARIDADE = [
        ('ensino_medio', 'Ensino Médio'),
        ('graduacao', 'Graduação'),
        ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado'),
    ]
    
    escolaridade = models.CharField(
        max_length=20, 
        choices=OPCOES_ESCOLARIDADE, 
        verbose_name="Escolaridade",
        null=False,
        blank=False
    )
    observacoes = models.TextField(verbose_name="Observações")
    curriculo = models.FileField(
        upload_to="projsesap/plataformacurriculos/curriculos", 
        verbose_name="Carregar o Currículo"
    )

    def __str__(self):
        return f"{self.primeironome} {self.ultimonome}"

    @property
    def mascara_telefone(self):
        if len(self.telefone) == 11:
            return f"({self.telefone[:2]}) {self.telefone[2:7]}-{self.telefone[7:]}"
        elif len(self.telefone) == 10:
            return f"({self.telefone[:2]}) {self.telefone[2:6]}-{self.telefone[6:]}"
        return self.telefone

# Formulário
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

    def clean_curriculo(self):
        curriculo = self.cleaned_data.get('curriculo')

        # Verificar extensões permitidas
        extensoes_permitidas = ['.doc', '.docx', '.pdf']
        if not any(curriculo.name.endswith(ext) for ext in extensoes_permitidas):
            raise ValidationError("Somente arquivos .doc, .docx ou .pdf são permitidos.")

        # Verificar tamanho máximo do arquivo
        max_tamanho = 1 * 1024 * 1024  # 1 MB
        if curriculo.size > max_tamanho:
            raise ValidationError("O tamanho máximo permitido para o arquivo é de 1 MB.")

        return curriculo