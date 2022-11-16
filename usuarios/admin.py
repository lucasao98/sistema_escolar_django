from django.contrib import admin
from usuarios.models import Aula, Diretor


class DiretorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome_diretor',
        'sobrenome_diretor',
        'email_diretor',
        'telefone_diretor',
        'id_instituicao',
        'criado_em',
        'editado_em'
    ]


class AulaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'horario_inicio',
        'horario_fim',
        'id_disciplina',
        'id_professor',
        'id_turma',
        'criado_em',
        'editado_em'
    ]

admin.site.register(Diretor, DiretorAdmin)
admin.site.register(Aula, AulaAdmin)
