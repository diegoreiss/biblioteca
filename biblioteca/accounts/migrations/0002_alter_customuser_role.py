# Generated by Django 4.2.7 on 2023-11-30 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Aluno'), (2, 'Gerente')], null=True),
        ),
    ]
