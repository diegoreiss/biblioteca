# Generated by Django 4.2.7 on 2023-12-03 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_email_alter_customuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_password_changed',
            field=models.BooleanField(default=False),
        ),
    ]
