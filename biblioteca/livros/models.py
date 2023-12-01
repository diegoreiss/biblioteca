from django.db import models

# Create your models here.

class Genero(models.Model):
    nome = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self) -> str:
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=255, unique=True, blank=False, null=False)
    genero = models.ForeignKey(Genero, on_delete=models.SET)
    paginas = models.PositiveIntegerField(blank=False, null=False)
    quantidade_estoque = models.PositiveIntegerField(blank=False, null=False)
    imagem = models.ImageField(blank=True, null=True)
    autor = models.ForeignKey(Autor, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.nome} - {self.quantidade_estoque}'
