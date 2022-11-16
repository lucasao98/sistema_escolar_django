from comum.models import BaseModel
from django.db import models

from instituicoes.models import Instituicao
from professores.models import Professor
from disciplinas.models import Disciplina
from turmas.models import Turma


class Diretor(BaseModel):
    nome_diretor = models.CharField(max_length=100, verbose_name="Nome do Diretor")
    sobrenome_diretor = models.CharField(max_length=255, verbose_name="Sobrenome do Diretor")
    email_diretor = models.CharField(max_length=100, verbose_name="Email do Diretor")
    telefone_diretor = models.CharField(max_length=50, verbose_name="Telefone do Diretor")
    id_instituicao = models.ForeignKey(
        Instituicao,
        on_delete=models.SET_NULL,
        related_name="diretores",
        verbose_name="Id da Instituição",
        null=True
    )


class Aula(BaseModel):
    horario_inicio = models.CharField(max_length=20, verbose_name="Horario de Inicio")
    horario_fim = models.CharField(max_length=20, verbose_name="Horario de Fim")
    id_disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.SET_NULL,
        related_name="aulas",
        verbose_name="Id da disciplina",
        null=True
    )
    id_professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        related_name="aulas",
        verbose_name="Id do professor",
        null=True
    )
    id_turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        related_name="aulas",
        verbose_name=" Id da turma",
        null=True
    )
