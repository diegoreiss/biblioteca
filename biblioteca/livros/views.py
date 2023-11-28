from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Autor, Genero


@login_required
def pagina_inicial(request):
    context = {
        "autores": Autor.objects.all(),
        "generos": Autor.objects.all()
    }

    return render(request, 'livros/pagina_inicial.html', context=context)


@login_required
def emprestimos(request):
    return render(request, 'livros/emprestimos.html')
