from comum.models import BaseModel
from django.db import models

from professores.models import Professor


class Turma(BaseModel):
    serie_turma = models.CharField(max_length=20, verbose_name="Série da Turma")
    identificador_turma = models.CharField(max_length=1, verbose_name="Identificador da Turma")
    quantidade_alunos = models.IntegerField(default=0)
    professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        related_name="turma",
        verbose_name="Id do professor",
        null=True
    )