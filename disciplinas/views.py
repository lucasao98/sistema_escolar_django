from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rolepermissions.decorators import has_role_decorator

from .models import Disciplina
from professores.models import Professor


@login_required()
@has_role_decorator('diretor', True)
def home_disciplinas(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            lista_disciplinas = Disciplina.objects.all()
            paginator = Paginator(lista_disciplinas, 5)

            page = request.GET.get('page')
            disciplinas= paginator.get_page(page)

            contexto = {
                "disciplinas": disciplinas
            }

            return render(request, 'disciplinas/home-disciplinas.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('diretor', True)
def tela_create_disciplina(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            professores = Professor.objects.all()

            contexto = {
                "professores": professores
            }
            return render(request, 'disciplinas/create-disciplina.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('diretor', True)
def create_disciplina(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            nova_disciplina = Disciplina.objects.create(
                nome_disciplina=request.POST['nome_disciplina'],
                professor_id=request.POST.get('professor_id')
            )

            nova_disciplina.save()

            return HttpResponseRedirect(reverse('disciplinas:home-disciplinas'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('diretor', True)
def tela_editar_disciplina(request: HttpRequest, id_disciplina: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            professores = Professor.objects.all()
            disciplina = Disciplina.objects.get(id=id_disciplina)

            contexto = {
                "professores": professores,
                "disciplina": disciplina
            }

            return render(request, 'disciplinas/editar-disciplina.html', contexto)
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('diretor', True)
def editar_disciplina(request: HttpRequest, id_disciplina: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            disciplina = Disciplina.objects.get(id=id_disciplina)

            if request.POST['nome']:
                disciplina.nome_disciplina = request.POST['nome']
            else:
                disciplina.nome_disciplina = disciplina.nome_disciplina

            if request.POST['professor_id']:
                disciplina.professor_id = request.POST['professor_id']
            else:
                disciplina.professor_id = disciplina.professor_id

            disciplina.save()

            return HttpResponseRedirect(reverse('disciplinas:home-disciplinas'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')


@login_required()
@has_role_decorator('diretor', True)
def deletar_disciplina(request: HttpRequest, id_disciplina: int) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            disciplina = Disciplina.objects.get(id=id_disciplina)

            disciplina.delete()

            return HttpResponseRedirect(reverse('disciplinas:home-disciplinas'))
        else:
            return render(request, 'layouts/login.html')
    else:
        return render(request, 'layouts/login.html')
