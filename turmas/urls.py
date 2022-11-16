from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_turmas, name="home-turmas"),
    path('tela-create-turma', views.tela_create_turma, name="tela-create-turma"),
    path('create-turma', views.create_turma, name="create-turma"),
    path('<int:id_turma>/edit', views.tela_editar_turmas, name="tela-editar-turma"),
    path('<int:id_turma>/edit-turma', views.editar_turma, name="editar-turma"),
    path('<int:id_turma>/delete-turma', views.deletar_turma, name="deletar-turma"),
]
