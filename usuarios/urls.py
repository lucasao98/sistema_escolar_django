from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_usuarios, name="home-usuarios"),
    path('tela-create-usuario', views.tela_create_usuario, name="tela-create-usuario"),
    path('create-usuario', views.create_usuario, name="create-usuario"),
    path('<int:id_usuario>/edit', views.editar_tela, name="editar-usuario-tela"),
    path('<int:id_usuario>/edit-usuario', views.editar_usuario, name="editar-usuario"),
    path('<int:id_usuario>/delete-usuario', views.deletar_usuario, name="deletar-usuario"),



]
