from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

from .models import CustomUser

from livros.views import pagina_inicial

# Create your views here.

@login_required
def criar_aluno(request):
    if request.POST:
        context = {'criar_aluno_status': 0}

        dados_aluno = {key: value for key, value in request.POST.copy().items()}
        dados_aluno['role'] = CustomUser.ALUNO
        del dados_aluno['csrfmiddlewaretoken']
        print(dados_aluno)

        try:
            user = CustomUser(**dados_aluno)
            user.set_password(user.password)
            user.save()

            context['criar_aluno_status'] = 200
        except IntegrityError as e:
            context['criar_aluno_status'] = 400

            return pagina_inicial(request, context)

        return pagina_inicial(request, context)

    return redirect('pagina-inicial')
