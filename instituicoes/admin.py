from django.contrib import admin

from .models import Instituicao


class InstituicaoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome_instituicao',
        'telefone_instituicao',
        'email_instituicao',
        'rua_instituicao',
        'cidade_instituicao',
        'pais_instituicao',
        'criado_em',
        'editado_em'
    ]


admin.site.register(Instituicao, InstituicaoAdmin)