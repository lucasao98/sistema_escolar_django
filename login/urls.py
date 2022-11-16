from django.urls import path
from . import views

urlpatterns = [
    path("",  views.tela_login, name='tela-login'),
    path("login_usuario",  views.login_usuario, name='login-usuario'),
    path("logout",  views.logout_usuario, name='logout-usuario'),
]
