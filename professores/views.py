from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator

from professores.models import Professor
from instituicoes.models import Instituicao


@login_required()
@has_role_decorator(['admin', 'diretor'], True)
def home_professores(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            lista_professores = Professor.objects.filter(is_active=1)
            contexto = {
                "lista_professores": lista_professores
            }

            return render(request, 'professores/home-professores.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor'], True)
def tela_create_professor(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            lista_instituicoes = Instituicao.objects.all()
            contexto = {
                'lista_instituicoes': lista_instituicoes
            }
            return render(request, 'professores/create-professor.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor'], True)
def create_professor(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            senha_professor = request.POST['senha_professor']
            username_professor = request.POST['username_professor']
            sobrenome_professor = request.POST['sobrenome_professor']
            email_professor = request.POST['email_professor']
            nome_professor = request.POST['nome_professor']
            telefone_professor = request.POST['telefone_professor']

            novo_usuario = User.objects.create_user(
                username=username_professor,
                email=email_professor,
                password=senha_professor,
                first_name=nome_professor,
                last_name=sobrenome_professor
            )

            professor = Professor.objects.create(
                nome_professor=nome_professor,
                sobrenome_professor=sobrenome_professor,
                email_professor=email_professor,
                telefone_professor=telefone_professor,
                instituicao_id=request.POST['instituicao_id'],
                is_active=1
            )

            novo_usuario.save()
            assign_role(novo_usuario, 'professor')

            professor.save()

            return HttpResponseRedirect(reverse('professores:home-professores'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor'], True)
def tela_editar_professor(request: HttpRequest, id_professor: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            professor = Professor.objects.get(id=id_professor)

            contexto = {
                "professor": professor
            }
            return render(request, 'professores/editar-professor.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor'], True)
def editar_professor(request: HttpRequest, id_professor: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            professor = Professor.objects.get(id=id_professor)

            if request.POST['nome']:
                professor.nome_professor = request.POST['nome']
            else:
                professor.nome_professor = professor.nome_professor

            if request.POST['sobrenome']:
                professor.sobrenome_professor = request.POST['sobrenome']
            else:
                professor.sobrenome_professor = professor.sobrenome_professor

            if request.POST['email']:
                professor.email_professor = request.POST['email']
            else:
                professor.email_professor = professor.email_professor

            if request.POST['telefone']:
                professor.telefone_professor = request.POST['telefone']
            else:
                professor.telefone_professor = professor.telefone_professor

            professor.save()

            return HttpResponseRedirect(reverse('professores:home-professores'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator(['admin', 'diretor'], True)
def deletar_professor(request: HttpRequest, id_professor: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            professor = Professor.objects.get(id=id_professor)

            professor.ativo = 0

            professor.save()

            return HttpResponseRedirect(reverse('professores:home-professores'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')
