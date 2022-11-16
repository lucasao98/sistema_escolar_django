from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator

from .models import Aluno
from turmas.models import Turma


@login_required()
@has_role_decorator(['admin', 'diretor', 'professor'], True)
def home_alunos(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            lista_alunos = Aluno.objects.order_by('nome_aluno').filter(is_active=1)

            contexto = {
                "lista_alunos": lista_alunos
            }

            return render(request, 'alunos/home-alunos.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor', 'professor'], True)
def tela_create_aluno(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            turmas = Turma.objects.all()

            contexto = {
                "turmas": turmas
            }
            return render(request, 'alunos/create-aluno.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor', 'professor'], True)
def create_aluno(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:

            novo_aluno = Aluno.objects.create(
                nome_aluno=request.POST['nome_aluno'],
                sobrenome_aluno=request.POST['sobrenome_aluno'],
                idade_aluno=request.POST['idade_aluno'],
                email_responsavel=request.POST['email_responsavel'],
                telefone_responsavel=request.POST['telefone_responsavel'],
                turma_id=request.POST['turma_id'],
                is_active=1
            )

            novo_usuario = User.objects.create_user(
                username=request.POST['username_aluno'],
                email=request.POST['email_responsavel'],
                password=request.POST['senha_aluno'],
                first_name=request.POST['nome_aluno'],
                last_name=request.POST['sobrenome_aluno'],
            )

            novo_usuario.save()
            assign_role(novo_usuario, 'aluno')

            novo_aluno.save()

            return HttpResponseRedirect(reverse('alunos:home-alunos'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor', 'professor'], True)
def tela_editar_aluno(request: HttpRequest, id_aluno: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            turmas = Turma.objects.all()
            aluno = Aluno.objects.get(id=id_aluno)
            usuario = User.objects.filter(email=aluno.email_responsavel)

            contexto = {
                "turmas": turmas,
                "aluno": aluno,
                "usuario": usuario
            }

            return render(request, 'alunos/editar-aluno.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor', 'professor'], True)
def editar_aluno(request: HttpRequest, id_aluno: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            aluno = Aluno.objects.get(id=id_aluno)

            if request.POST['nome']:
                aluno.nome_aluno = request.POST['nome']
            else:
                aluno.nome_aluno = aluno.nome_aluno

            if request.POST['sobrenome']:
                aluno.sobrenome_aluno = request.POST['sobrenome']
            else:
                aluno.sobrenome_aluno = aluno.sobrenome_aluno

            if request.POST['idade_aluno']:
                aluno.idade_aluno = request.POST['idade_aluno']
            else:
                aluno.idade_aluno = aluno.idade_aluno

            if request.POST['email_responsavel']:
                aluno.email_responsavel = request.POST['email_responsavel']
            else:
                aluno.email_responsavel = aluno.email_responsavel

            if request.POST['telefone_responsavel']:
                aluno.email_responsavel = request.POST['telefone_responsavel']
            else:
                aluno.telefone_responsavel = aluno.telefone_responsavel

            if request.POST['turma_id']:
                aluno.turma_id = request.POST['turma_id']
            else:
                aluno.turma_id = aluno.turma_id

            aluno.save()

            return HttpResponseRedirect(reverse('alunos:home-alunos'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor', 'professor'], True)
def deletar_aluno(request: HttpRequest, id_aluno: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            aluno = Aluno.objects.get(id=id_aluno)

            aluno.is_active = 0

            aluno.save()

            return HttpResponseRedirect(reverse('alunos:home-alunos'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')
