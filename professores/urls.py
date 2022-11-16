from django.urls import path

from . import views

urlpatterns = [
    path('professores', views.home_professores, name="home-professores"),
    path('tela-create-professor', views.tela_create_professor, name="tela-create-professor"),
    path('create-professor', views.create_professor, name="create-professor"),
    path('<int:id_professor>/edit', views.tela_editar_professor, name="tela-editar-professor"),
    path('<int:id_professor>/edit-professor', views.editar_professor, name="editar-professor"),
    path('<int:id_professor>/delete-professor', views.deletar_professor, name="deletar-professor")
]
