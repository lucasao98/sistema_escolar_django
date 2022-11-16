from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_alunos, name="home-alunos"),
    path('tela-create-aluno', views.tela_create_aluno, name="tela-create-aluno"),
    path('create-aluno', views.create_aluno, name="create-aluno"),
    path('<int:id_aluno>/edit', views.tela_editar_aluno, name="tela-editar-aluno"),
    path('<int:id_aluno>/edit-aluno', views.editar_aluno, name="editar-aluno"),
    path('<int:id_aluno>/delete-aluno', views.deletar_aluno, name="deletar-aluno"),

]
