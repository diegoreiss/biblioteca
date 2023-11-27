from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def pagina_inicial(request):
    return render(request, 'livros/pagina_inicial.html')


@login_required
def emprestimos(request):
    return render(request, 'livros/emprestimos.html')
