from django.contrib import admin

from .models import Aluno


class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome_aluno',
        'sobrenome_aluno',
        'idade_aluno',
        'email_responsavel',
        'telefone_responsavel',
        'turma',
        'criado_em',
        'editado_em'
    ]


admin.site.register(Aluno, AlunoAdmin)
