from comum.models import BaseModel
from django.db import models

from professores.models import Professor


class Disciplina(BaseModel):
    nome_disciplina = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        related_name="disciplinas",
        verbose_name="Id da Professor",
        null=True
    )
