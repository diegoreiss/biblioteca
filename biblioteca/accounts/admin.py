from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password

from .models import CustomUser

class CustomAdmin(UserAdmin):
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.password = make_password(form.cleaned_data['password'])
        return super().save_model(request, obj, form, change)

# Register your models here.


admin.site.register(CustomUser, UserAdmin)
