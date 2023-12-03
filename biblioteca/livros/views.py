from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

from .models import Autor, Genero, Livro
from accounts.decorators import password_changed_required


ITEMS_POR_PAGINA = 10

context_autores_generos = {
    "autores": Autor.objects.all,
    "generos": Genero.objects.all
}


@login_required
@password_changed_required
def pagina_inicial(request, newContext={}):
    numero_pagina = int(request.GET.get('page')) if request.GET.get('page') else 1

    paginator = Paginator(Livro.objects.all(), ITEMS_POR_PAGINA)
    paginator_el = list(paginator.get_elided_page_range(numero_pagina, on_each_side=3, on_ends=1))
    pagina = paginator.get_page(numero_pagina)

    context = {key: value() for key, value in context_autores_generos.items()}
    context.update(newContext)
    context.update({
        'pagina_atual': numero_pagina,
        'total_paginas': paginator.num_pages,
        'pagina_array': paginator_el,
        'dados_pagina': pagina
    })   

    return render(request, 'livros/pagina_inicial.html', context=context)


@login_required
@password_changed_required
def detalhes_livro(request, id):
    context = {
        'livro': Livro.objects.get(id=id)
    }

    return render(request, 'livros/detalhe_livro.html', context=context)


@login_required
@password_changed_required
def emprestimos(request):
    return render(request, 'livros/emprestimos.html')


@login_required
@password_changed_required
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

        context['criar_genero_status'] = 200

        return pagina_inicial(request, context)
    
    return pagina_inicial(request)


@login_required
@password_changed_required
def criar_autor(request):
    if request.POST:
        context = {'criar_autor_status': 0}
        nome = request.POST['nome']

        if not nome:
            context['criar_autor_status'] = 400
            return pagina_inicial(request, context)
        
        try:
            Autor.objects.create(nome=nome)
        except IntegrityError as e:
            context['criar_autor_status'] = 400

            return pagina_inicial(request, context)
        
        context['criar_autor_status'] = 200
        
        return pagina_inicial(request, context)

    return pagina_inicial(request)


@login_required
@password_changed_required
def criar_livro(request):
    if request.POST:
        context = {'criar_livro_status': 0}

        if not all(request.POST.values()):
            context['criar_livro_status'] = 400

            return pagina_inicial(request, context)

        dados_livro = {key: int(value) if str(value).isnumeric() else value for key, value in request.POST.items()}
        dados_livro['imagem'] = request.FILES.get('imagem')
        del dados_livro['csrfmiddlewaretoken']
        
        try:
            Livro.objects.create(**dados_livro)

            context['criar_livro_status'] = 200
        except IntegrityError as e:
            context['criar_livro_status'] = 400

            return pagina_inicial(request, context)
        
        return pagina_inicial(request, context)
    
    return pagina_inicial(request)
