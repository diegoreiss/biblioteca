from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina-inicial'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('genero/criar', views.criar_genero, name='criar-genero'),
    path('autor/criar', views.criar_autor, name='criar-autor'),
    path('livro/criar', views.criar_livro, name='criar-livro'),
    path('livro/<int:id>/', views.detalhes_livro, name='detalhes-livro')
]
