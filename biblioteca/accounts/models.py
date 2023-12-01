from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(AbstractUser):
    ALUNO = 1
    GERENTE = 2

    ROLE_CHOICES = (
        (ALUNO, 'Aluno'),
        (GERENTE, 'Gerente')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    def create(self, validated_data):
        user = User.objects.create(email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user
