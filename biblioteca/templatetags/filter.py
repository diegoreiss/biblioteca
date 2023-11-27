from django import template


register = template.Library()


@register.filter
def esta_no_grupo(usuario, grupo):
    print("oi")
    return usuario.groups.filter(name=grupo).exists()
