from django.db import models
from django.db.models import F
from django.core.exceptions import ValidationError

# Create your models here.

class Genero(models.Model):
    class Meta:
        ordering = [F('id').asc()]

    nome = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.nome


class Autor(models.Model):
    class Meta:
        ordering = [F('id').asc()]
        
    nome = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self) -> str:
        return self.nome


class Livro(models.Model):
    class Meta:
        ordering = [F('id').asc()]

    nome = models.CharField(max_length=255, unique=True, blank=False, null=False)
    genero = models.ForeignKey(Genero, on_delete=models.SET)
    paginas = models.PositiveIntegerField(blank=False, null=False)
    quantidade_estoque = models.PositiveIntegerField(blank=False, null=False)
    imagem = models.ImageField(blank=True, null=True)
    autor = models.ForeignKey(Autor, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.nome} - {self.quantidade_estoque}'


class Emprestimo(models.Model):
    class Meta:
        ordering = [F('id').asc()]

    aluno = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, blank=False, null=False)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, blank=False, null=False)

    def clean(self) -> None:
        if self.aluno.is_superuser or (self.aluno.role == None or self.aluno.role == 2):
            raise ValidationError('Apenas alunos podem fazer empréstimos!', code='invalid')
            
        if Emprestimo.objects.filter(aluno_id=self.aluno.id, livro_id=self.livro.id):
            raise ValidationError(f'Aluno {self.aluno.username} já realizou o empréstimo desse livro!', code='invalid')

        return super().clean()

    def __str__(self) -> str:
        return f'{self.aluno.username} - {self.livro.nome}'