from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.contrib.sites.models import RequestSite
from django.http import Http404

from registration.backends.default.views import RegistrationView
from registration import signals
from registration.models import RegistrationProfile

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


class AppUserRegistrationView(RegistrationView):
    def register(self, request, **cleaned_data):
        username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(email, username, password, site)
        signals.user_registered.send(sender=self.__class__, user=new_user, request=request)

        return new_user
