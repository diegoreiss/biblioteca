from django.urls import path

from . import views

urlpatterns = [
    path('aluno/criar', views.criar_aluno, name='criar-aluno'),
]
