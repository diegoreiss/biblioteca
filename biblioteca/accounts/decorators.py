from django.shortcuts import redirect


def password_changed_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_password_changed:
            return redirect('retype-password')
        
        return function(request, *args, **kwargs)
        
    return wrapper
    