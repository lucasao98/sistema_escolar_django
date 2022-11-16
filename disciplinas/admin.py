from django.contrib import admin

from .models import Disciplina


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome_disciplina',
        'professor',
        'criado_em',
        'editado_em'
    ]


admin.site.register(Disciplina, DisciplinaAdmin)
