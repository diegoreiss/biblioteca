from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

from .models import Autor, Genero


context_autores_generos = {
    "autores": Autor.objects.all,
    "generos": Genero.objects.all
}


@login_required
def pagina_inicial(request, newContext={}):
    context = {key: value() for key, value in context_autores_generos.items()}
    context.update(newContext)

    return render(request, 'livros/pagina_inicial.html', context=context)


@login_required
def emprestimos(request):
    return render(request, 'livros/emprestimos.html')


@login_required
def criar_genero(request):
    if request.POST:
        context = {'criar_genero_status': 0}
        nome = request.POST['nome']

        if not nome:
            context['criar_genero_status'] = 400
            return pagina_inicial(request, context)

        try:
            Genero.objects.create(nome=nome)
        except IntegrityError as e:
            context['criar_genero_status'] = 400
            return pagina_inicial(request, context)
            ...
        context['criar_genero_status'] = 200

        return pagina_inicial(request, context)
    
    return pagina_inicial(request)
