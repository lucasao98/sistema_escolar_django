"""projeto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('login.urls', 'login'), namespace='login')),
    path('home/', include(('home.urls', 'home'), namespace='home')),
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('instituicoes/', include(('instituicoes.urls', 'instituicoes'), namespace='instituicoes')),
    path('professores/', include(('professores.urls', 'professores'), namespace='professores')),
    path('disciplinas/', include(('disciplinas.urls', 'disciplinas'), namespace='disciplinas')),
    path('turmas/', include(('turmas.urls', 'turmas'), namespace='turmas')),
    path('alunos/', include(('alunos.urls', 'alunos'), namespace='alunos')),
]
