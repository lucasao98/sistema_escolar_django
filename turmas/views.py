from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rolepermissions.decorators import has_role_decorator

from .models import Turma
from professores.models import Professor
from alunos.models import Aluno


@login_required()
@has_role_decorator(['diretor', 'professor'], True)
def home_turmas(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            lista_turmas = Turma.objects.all()

            contexto = {
                "lista_turmas": lista_turmas
            }

            return render(request, 'turmas/home-turmas.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['diretor', 'professor'], True)
def tela_create_turma(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            professores = Professor.objects.filter(is_active=1)

            contexto = {
                "professores": professores
            }

            return render(request, 'turmas/create-turma.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['diretor', 'professor'], True)
def create_turma(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            nova_turma = Turma.objects.create(
                serie_turma=request.POST['serie_turma'],
                identificador_turma=request.POST['identificador_turma'],
                quantidade_alunos=request.POST['quantidade_alunos'],
                professor_id=request.POST['professor_id']
            )

            nova_turma.save()

            return HttpResponseRedirect(reverse('turmas:home-turmas'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['diretor', 'professor'], True)
def tela_editar_turmas(request: HttpRequest, id_turma: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            professores = Professor.objects.all()
            turma = Turma.objects.get(id=id_turma)

            contexto = {
                "professores": professores,
                "turma": turma
            }

            return render(request, 'turmas/editar-turma.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['diretor', 'professor'], True)
def editar_turma(request: HttpRequest, id_turma: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            turma = Turma.objects.get(id=id_turma)

            if request.POST['serie_turma']:
                turma.serie_turma = request.POST['serie_turma']
            else:
                turma.serie_turma = turma.serie_turma

            if request.POST['identificador_turma']:
                turma.identificador_turma = request.POST['identificador_turma']
            else:
                turma.identificador_turma = turma.identificador_turma

            if request.POST['quantidade_alunos']:
                turma.quantidade_alunos = request.POST['quantidade_alunos']
            else:
                turma.quantidade_alunos = turma.quantidade_alunos

            if request.POST['professor_id']:
                turma.professor_id = request.POST['professor_id']

            turma.save()

            return HttpResponseRedirect(reverse('turmas:home-turmas'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['diretor', 'professor'], True)
def deletar_turma(request: HttpRequest, id_turma: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            turma = Turma.objects.get(id=id_turma)

            turma.delete()

            return HttpResponseRedirect(reverse('turmas:home-turmas'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')
