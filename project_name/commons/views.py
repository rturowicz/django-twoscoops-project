from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.cache import never_cache


@never_cache
def robots(request):
    return render_to_response(
        'commons/robots.txt',
        {},
        context_instance=RequestContext(request)
    )
