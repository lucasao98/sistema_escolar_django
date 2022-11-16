from comum.models import BaseModel
from django.db import models

from turmas.models import Turma


class Aluno(BaseModel):
    nome_aluno = models.CharField(max_length=255, verbose_name="Nome do Aluno")
    sobrenome_aluno = models.CharField(max_length=255, verbose_name="Nome do Sobrenome")
    idade_aluno = models.IntegerField(null=True)
    email_responsavel = models.CharField(max_length=100, verbose_name="Email do Responsavel")
    telefone_responsavel = models.CharField(max_length=50, verbose_name="Telefone do Responsavel")
    is_active = models.IntegerField(default=1, verbose_name="Ativo")
    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        related_name="disciplina",
        verbose_name=" Id da turma",
        null=True
    )
