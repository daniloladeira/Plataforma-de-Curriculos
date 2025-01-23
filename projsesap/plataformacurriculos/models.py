from django.db import models

# Crie seus modelos aqui.

class Candidato(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(max_length=100, verbose_name="E-Mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    posicao_desejada = models.CharField(max_length=100, verbose_name="Posição Desejada")
    OPCOES_ESCOLARIDADE = [
        ('ensino_medio', 'Ensino Médio'),
        ('graduacao', 'Graduação'),
        ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado'),
    ]
    escolaridade = models.CharField(max_length=100, choices=OPCOES_ESCOLARIDADE, verbose_name="Escolaridade")
    observacoes = models.TextField(max_length=100, verbose_name="Observações")
    arquivo_curriculo = models.FileField(upload_to="projsesap/plataformacurriculos/curriculos", verbose_name="Carregar o Currículo")

    def __str__(self):
        return self.nome
    
    @property
    def mascara_telefone(self):
        return f"({self.telefone[:2]}) {self.telefone[2:6]}-{self.telefone[6:]}"
