from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from functools import wraps

def professor():
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            # if Professor.objects.filter(user=request.user).exists():
            if True:
                return func(request, *args, **kwargs)
            else:
                raise Http404

        return wraps(func)(inner_decorator)

    return decorator
