from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_instituicoes, name="home-instituicoes"),
    path('tela-create-instituicao', views.tela_create_instituicao, name="tela-create-instituicao"),
    path('create-instituicao', views.create_instituicao, name="create-instituicao"),
    path('<int:id_instituicao>/edit', views.tela_editar_instituicao, name="tela-editar-instituicao"),
    path('<int:id_instituicao>/edit-instituicao', views.editar_instituicao, name="editar-instituicao"),
    path('<int:id_instituicao>/delete-instituicao', views.deletar_instituicao, name="deletar-instituicao"),

]
