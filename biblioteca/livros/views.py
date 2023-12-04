from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

from .models import Autor, Genero, Livro, Emprestimo
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
    livro_like = request.GET.get('livroLike')

    paginator = Paginator(Livro.objects.filter(quantidade_estoque__gt=0).all(), ITEMS_POR_PAGINA)

    if livro_like:
        paginator = Paginator(Livro.objects.filter(quantidade_estoque__gt=0, nome__contains=livro_like).all(), ITEMS_POR_PAGINA)

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

    if request.user.role == 1:
        query = Emprestimo.objects.filter(aluno_id=request.user.id).all().values_list('livro_id', flat=True)
        context.update({'livros_relacionados': list(query)})
    
    print(context)

    return render(request, 'livros/pagina_inicial.html', context=context)


@login_required
@password_changed_required
def detalhes_livro(request, id):
    context = {
        'livro': Livro.objects.get(id=id)
    }

    if request.user.role == 1:
        context.update({'aluno_tem': Emprestimo.objects.filter(aluno_id=request.user.id, livro_id=id).exists()})

    if context['livro'].quantidade_estoque <= 0:
        return redirect('pagina-inicial')
    
    return render(request, 'livros/detalhe_livro.html', context=context)


@login_required
@password_changed_required
def pegar_livro_emprestado(request, id):
    context = {'criar_emprestimo_status': 0}

    if request.POST:
        if Emprestimo.objects.filter(aluno_id=request.user.id, livro_id=id):
            context['criar_emprestimo_status'] = 400

            return pagina_inicial(request, context)

        try:
            Emprestimo.objects.create(aluno_id=request.user.id, livro_id=id)
            context['criar_emprestimo_status'] = 200
        except:
            context['criar_emprestimo_status'] = 400

        return pagina_inicial(request, context)
    
    return detalhes_livro(request, id)


@login_required
@password_changed_required
def devolver_livro_emprestado(request, id):
    context = {'devolver_livro_emprestado_status': 0}

    if request.POST:
        query = Emprestimo.objects.filter(aluno_id=request.user.id, livro_id=id).first()

        if not query:
            context['devolver_livro_emprestado_status'] = 400

            return pagina_inicial(request, context)
        
        try:
            query.delete()
            context['devolver_livro_emprestado_status'] = 200
        except:
            context['devolver_livro_emprestado_status'] = 400

        return pagina_inicial(request, context)
    
    return detalhes_livro(request, id)


@login_required
@password_changed_required
def emprestimos(request):
    numero_pagina = int(request.GET.get('page', 1))
    emprestimo_livro_like = request.GET.get('emprestimoLivroLike')

    def filtrar_por_user():
        print(emprestimo_livro_like)
        if request.user.role == 1:
            paginator = Paginator(Emprestimo.objects.filter(aluno_id=request.user.id).all(), ITEMS_POR_PAGINA)
            
            if emprestimo_livro_like:
                paginator = Paginator(Emprestimo.objects.filter(aluno_id=request.user.id, livro__nome__contains=emprestimo_livro_like).all(), ITEMS_POR_PAGINA)
            
            return paginator
        
        elif request.user.role == 2:
            paginator = Paginator(Emprestimo.objects.all(), ITEMS_POR_PAGINA)

            if emprestimo_livro_like:
                paginator = Paginator(Emprestimo.objects.filter(livro__nome__contains=emprestimo_livro_like).all(), ITEMS_POR_PAGINA)

            return paginator

    paginator = filtrar_por_user()
    
    paginator_el = list(paginator.get_elided_page_range(numero_pagina, on_each_side=3, on_ends=1))
    pagina = paginator.get_page(numero_pagina)

    context = {
        'pagina_atual': numero_pagina,
        'total_paginas': paginator.num_pages,
        'pagina_array': paginator_el,
        'emprestimos': pagina
    }

    return render(request, 'livros/emprestimos.html', context=context)


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
