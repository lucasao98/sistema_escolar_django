from comum.models import BaseModel
from django.db import models


class Instituicao(BaseModel):
    nome_instituicao = models.CharField(max_length=255, verbose_name="Nome da Instituição")
    telefone_instituicao = models.CharField(max_length=30, verbose_name="Telefone da Instituição")
    email_instituicao = models.CharField(max_length=50, verbose_name="Email da Instituição", unique=True)
    rua_instituicao = models.CharField(max_length=255, verbose_name="Rua da Instituição")
    cidade_instituicao = models.CharField(max_length=100, verbose_name="Cidade da Instituição")
    pais_instituicao = models.CharField(max_length=100, verbose_name="País da Instituição")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return f"{self.id}.{self.nome_instituicao}"
