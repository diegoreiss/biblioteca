from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('retypepassword/', views.retype_password, name='retype-password'),
    path('aluno/criar', views.criar_aluno, name='criar-aluno'),
]
