from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_disciplinas, name="home-disciplinas"),
    path('tela-create-disciplina', views.tela_create_disciplina, name="tela-create-disciplina"),
    path('create-disciplina', views.create_disciplina, name="create-disciplina"),
    path('<int:id_disciplina>/edit', views.tela_editar_disciplina, name="tela-editar-disciplina"),
    path('<int:id_disciplina>/edit-disciplina', views.editar_disciplina, name="editar-disciplina"),
    path('<int:id_disciplina>/delete-disciplina', views.deletar_disciplina, name="deletar-disciplina"),

]
