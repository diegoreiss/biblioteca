from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

from .utils import email_utils

# Create your models here.

class CustomUser(AbstractUser):
    ALUNO = 1
    GERENTE = 2

    ROLE_CHOICES = (
        (ALUNO, 'Aluno'),
        (GERENTE, 'Gerente')
    )

    email = models.EmailField(_("email address"), blank=False, null=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    password = models.CharField(max_length=255, validators=[
        MinLengthValidator(8, 'Mínimo 8 caracteres')
    ])
    prev_password = models.CharField(max_length=255, blank=True, null=True)
    is_password_changed = models.BooleanField(default=False, blank=False, null=False)

    def set_password(self, raw_password: str | None) -> None:
        self.prev_password = raw_password
        self.is_password_changed = False

        return super().set_password(raw_password)

    def save(self, retype_password=False, *args, **kwargs):
        plain_text_password = self.prev_password

        if retype_password or self.is_superuser:
            self.is_password_changed = True

        self.prev_password = None
        super(CustomUser, self).save(*args, **kwargs)

        if not self.is_superuser:
            content = "Muito obrigado por usar o nosso sistema!\n" + \
            "A seguir os seus dados de autenticação provisórios:\n\n" + \
            f"usuario: {self.username}\n" + \
            f"senha: {plain_text_password} (Trocar a senha após o login)"
            dados_email = ('Criação de conta na Biblioteca', self.email, content)
            email_utils.send_email(*dados_email)
