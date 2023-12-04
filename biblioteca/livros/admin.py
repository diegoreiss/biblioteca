from django.contrib import admin

from .models import Genero, Autor, Livro, Emprestimo

# Register your models here.

admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Emprestimo)
