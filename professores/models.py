from comum.models import BaseModel
from django.db import models

from instituicoes.models import Instituicao


class Professor(BaseModel):
    nome_professor = models.CharField(max_length=100, verbose_name="Nome do Professor")
    sobrenome_professor = models.CharField(max_length=255, verbose_name="Sobrenome do Professor")
    email_professor = models.CharField(max_length=100, verbose_name="Email do Professor")
    telefone_professor = models.CharField(max_length=50, verbose_name="Telefone do Professor")
    is_active = models.BooleanField(default=0)
    instituicao = models.ForeignKey(
        Instituicao,
        on_delete=models.SET_NULL,
        related_name="professores",
        verbose_name="Id da Instituição",
        null=True,
    )
