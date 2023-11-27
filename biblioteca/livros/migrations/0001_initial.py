# Generated by Django 4.2.7 on 2023-11-27 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('paginas', models.PositiveIntegerField()),
                ('quantidade_estoque', models.PositiveIntegerField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
                ('autores', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livros.autor')),
                ('genero', models.OneToOneField(on_delete=django.db.models.deletion.SET, to='livros.genero')),
            ],
        ),
    ]
