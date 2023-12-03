from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

# Create your models here.

class CustomUser(AbstractUser):
    ALUNO = 1
    GERENTE = 2

    ROLE_CHOICES = (
        (ALUNO, 'Aluno'),
        (GERENTE, 'Gerente')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    password = models.CharField(max_length=255, validators=[
        MinLengthValidator(8, 'Mínimo 8 caracteres')
    ])
    is_password_changed = models.BooleanField(default=False, blank=False, null=False)

    def set_password(self, raw_password: str | None) -> None:
        self.is_password_changed = False

        return super().set_password(raw_password)

    def save(self, retype_password=False, *args, **kwargs):
        if retype_password:
            self.is_password_changed = True

        return super(CustomUser, self).save(*args, **kwargs)
