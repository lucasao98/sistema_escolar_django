from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_usuario(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        usuario = request.POST["username"]
        senha = request.POST["password"]

        contexto = {
            "message": "Usuário não encontrado"
        }

        auth = authenticate(request, username=usuario, password=senha)

        if not auth:
            return render(request, "layouts/login.html", contexto)

        contexto = {
            "usuario": auth
        }
        login(request, auth)

        return render(request, 'home.html', contexto)
    else:
        return render(request, "layouts/login.html")


def tela_login(request: HttpRequest) -> HttpResponse:
    return render(request, 'layouts/login.html')


@login_required()
def logout_usuario(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
            return render(request, 'layouts/login.html')
        else:
            return render(request, 'layouts/login.html')
