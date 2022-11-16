from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def home(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            return render(request, 'home.html')
        else:
            return HttpResponseRedirect(reverse('login:tela-login'))
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'home.html')
        else:
            return render(request, 'layouts/login.html')

