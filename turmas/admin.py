from django.contrib import admin

from .models import Turma


class TurmaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'serie_turma',
        'identificador_turma',
        'quantidade_alunos',
        'professor',
        'criado_em',
        'editado_em'
    ]


admin.site.register(Turma, TurmaAdmin)
