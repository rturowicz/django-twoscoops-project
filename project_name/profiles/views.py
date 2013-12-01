from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import AppUser


@login_required
def index(request):

    return render_to_response(
        'profiles/index.html',
        {},
        context_instance=RequestContext(request)
    )


def user(request, user_id):
    try:
        user = AppUser.objects.get(pk=user_id)

        return render_to_response(
            'profiles/user.html',
            {'user_obj': user},
            context_instance=RequestContext(request)
        )
    except AppUser.DoesNotExist, e:
        raise Http404
