from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina-inicial'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('genero/criar', views.criar_genero, name='criar-genero')
]
