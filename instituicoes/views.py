from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rolepermissions.decorators import has_role_decorator

from instituicoes.models import Instituicao


@login_required()
@has_role_decorator('admin', True)
def home_instituicoes(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            lista_instituicoes = Instituicao.objects.filter(is_active=1)

            contexto = {
                "lista_instituicoes": lista_instituicoes
            }

            return render(request, 'instituicoes/home-instituicoes.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def tela_create_instituicao(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'instituicoes/create-instituicao.html')
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def create_instituicao(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            nova_instituicao = Instituicao.objects.create(
                nome_instituicao=request.POST['nome_instituicao'],
                telefone_instituicao=request.POST['telefone_instituicao'],
                email_instituicao=request.POST['email_instituicao'],
                rua_instituicao=request.POST['rua_instituicao'],
                cidade_instituicao=request.POST['cidade_instituicao'],
                pais_instituicao=request.POST['pais_instituicao']
            )

            nova_instituicao.save()

            return HttpResponseRedirect(reverse('instituicoes:home-instituicoes'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def tela_editar_instituicao(request: HttpRequest, id_instituicao: int) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            instituicao = Instituicao.objects.get(id=id_instituicao)

            contexto = {
                "instituicao": instituicao
            }
            return render(request, 'instituicoes/editar-instituicao.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def editar_instituicao(request: HttpRequest, id_instituicao: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            instituicao = Instituicao.objects.get(id=id_instituicao)

            if request.POST['nome']:
                instituicao.nome_instituicao = request.POST['nome']
            else:
                instituicao.nome_instituicao = instituicao.nome_instituicao

            if request.POST['telefone']:
                instituicao.telefone_instituicao = request.POST['telefone']
            else:
                instituicao.telefone_instituicao = instituicao.telefone_instituicao

            if request.POST['email']:
                instituicao.email_instituicao = request.POST['email']
            else:
                instituicao.email_instituicao = instituicao.email_instituicao

            if request.POST['rua']:
                instituicao.rua_instituicao = request.POST['rua']
            else:
                instituicao.rua_instituicao = instituicao.rua_instituicao

            if request.POST['cidade']:
                instituicao.cidade_instituicao = request.POST['cidade']
            else:
                instituicao.cidade_instituicao = instituicao.cidade_instituicao

            if request.POST['pais']:
                instituicao.pais_instituicao = request.POST['pais']
            else:
                instituicao.pais_instituicao = instituicao.pais_instituicao

            instituicao.save()

            return HttpResponseRedirect(reverse('instituicoes:home-instituicoes'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def deletar_instituicao(request: HttpRequest, id_instituicao: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            instituicao = Instituicao.objects.get(id=id_instituicao)

            instituicao.is_active = 0

            instituicao.save()

            return HttpResponseRedirect(reverse('instituicoes:home-instituicoes'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')
