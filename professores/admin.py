from django.contrib import admin

from .models import Professor


class ProfessorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome_professor',
        'sobrenome_professor',
        'email_professor',
        'telefone_professor',
        'instituicao',
        'criado_em',
        'editado_em'
    ]


admin.site.register(Professor, ProfessorAdmin)
