from django.core.exceptions import PermissionDenied

def employer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.profile.role != 'employer':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper


def seeker_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.profile.role != 'seeker':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper
