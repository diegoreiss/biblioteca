from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.utils import IntegrityError

from .models import CustomUser
from .decorators import password_changed_required

from livros.views import pagina_inicial


def login(request):
    redirect_url_name = 'pagina-inicial'
    redirect_login_url_name = 'login'
    redirect_retypepassword_url_name = 'retype-password'

    if request.user.is_authenticated:
        print('ta autenticado')
        return redirect(redirect_url_name)

    rpost = request.POST
    if rpost:
        dados_login = {key: value for key, value in rpost.copy().items()}
        del dados_login['csrfmiddlewaretoken']
        
        if not all(dados_login.values()):
            return redirect(redirect_login_url_name)

        user_verify = auth.authenticate(request, **dados_login)

        if user_verify is None:
            messages.error(request, 'Credenciais inválidas')

            return redirect(redirect_login_url_name)
        
        auth.login(request, user_verify)

        if user_verify.is_superuser:
            return redirect('admin:index')

        if not user_verify.is_password_changed:
            return redirect(redirect_retypepassword_url_name)
        
        return redirect(redirect_url_name)

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)

    return redirect('login')


@login_required
def retype_password(request):
    redirect_retype_url_name = 'retype-password'
    rpost = request.POST

    if rpost:
        dados_form = {key: value for key, value in rpost.copy().items()}
        del dados_form['csrfmiddlewaretoken']

        senhas = set(dados_form.values())
        if len(senhas) != 1:
            messages.error(request, 'Senhas não conferem')

            return redirect(redirect_retype_url_name)

        if request.user.check_password(*senhas):
            messages.error(request, 'Senha não pode ser a mesma que a antiga!')

            return redirect(redirect_retype_url_name)
        
        if len(*senhas) < 8:
            messages.error(request, 'Senha precisa ser maior que 8 caracteres!')
        
        try:
            request.user.set_password(*senhas)
            request.user.save(retype_password=True)
        except BaseException as e:
            raise e

        messages.success(request, 'Senha alterada com sucesso!')
        return redirect('login')

    return render(request, 'registration/retype_password.html')


@login_required
@password_changed_required
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
