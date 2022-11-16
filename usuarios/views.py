from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator


@login_required()
@has_role_decorator('admin', True)
def home_usuarios(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            lista_usuarios = User.objects.order_by('first_name').filter(is_active=1)
            paginator = Paginator(lista_usuarios, 5)

            page = request.GET.get('page')
            usuarios = paginator.get_page(page)

            contexto = {
                "usuarios": usuarios
            }

            return render(request, 'usuarios/home-usuarios.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def tela_create_usuario(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'usuarios/create-usuario.html')
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def create_usuario(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            funcao_usuario = request.POST['funcao-usuario']
            senha_novo_usuario = request.POST['senha_usuario']
            username_novo_usuario = request.POST['username_usuario']
            sobrenome_novo_usuario = request.POST['sobrenome_usuario']
            email_novo_usuario = request.POST['email_usuario']
            nome_novo_usuario = request.POST['nome_usuario']

            novo_usuario = User.objects.create_user(
                username_novo_usuario,
                email_novo_usuario,
                senha_novo_usuario,
            )

            novo_usuario.last_name = sobrenome_novo_usuario
            novo_usuario.first_name = nome_novo_usuario
            novo_usuario.is_active = 1

            novo_usuario.save()
            assign_role(novo_usuario, funcao_usuario)

            return HttpResponseRedirect(reverse('usuarios:home-usuarios'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def editar_tela(request: HttpRequest, id_usuario: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            usuario = User.objects.get(id=id_usuario)

            contexto = {
                "usuario": usuario
            }
            return render(request, 'usuarios/editar-usuario.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def editar_usuario(request: HttpRequest, id_usuario: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            usuario = User.objects.get(id=id_usuario)

            if request.POST['nome']:
                usuario.first_name = request.POST['nome']
            else:
                usuario.first_name = usuario.first_name

            if request.POST['sobrenome']:
                usuario.last_name = request.POST['sobrenome']
            else:
                usuario.last_name = usuario.last_name

            if request.POST['superuser']:
                usuario.is_superuser = request.POST['superuser']
            else:
                usuario.is_superuser = usuario.is_superuser

            usuario.save()

            return HttpResponseRedirect(reverse('usuarios:home-usuarios'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('admin', True)
def deletar_usuario(request: HttpRequest, id_usuario: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            usuario = User.objects.get(id=id_usuario)

            usuario.is_active = 0

            usuario.save()

            return HttpResponseRedirect(reverse('usuarios:home-usuarios'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')
