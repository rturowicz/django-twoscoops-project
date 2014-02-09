from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as django_login, logout as django_logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset as django_password_reset
from django.contrib.auth.views import password_reset_done as django_password_reset_done
from django.contrib.auth.views import password_reset_confirm as django_password_reset_confirm
from django.contrib.auth.views import password_reset_complete as django_password_reset_complete
from django.contrib.auth.views import password_change as django_password_change
from django.contrib.auth.views import password_change_done as django_password_change_done
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

from ratelimit.decorators import ratelimit


@never_cache
def robots(request):
    return render_to_response(
        'commons/robots.txt',
        {},
        context_instance=RequestContext(request)
    )


@csrf_protect
@never_cache
@ratelimit(
    field='username', ip=False, rate='2/m', method="POST",
    block=True
)
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return django_login(request, template_name='commons/login.html')


def logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return django_logout(request, template_name='commons/logout.html')


@csrf_protect
def password_reset(request):
    return django_password_reset(
        request,
        template_name='commons/password_reset_form.html',
        email_template_name='commons/password_reset_email.html',
        subject_template_name='commons/password_reset_subject.txt',
        post_reset_redirect=reverse('password_reset_done_view')
    )


@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb36=None, token=None):
    return django_password_reset_confirm(
        request, uidb36, token,
        template_name='commons/password_reset_confirm.html',
        post_reset_redirect=reverse('password_reset_complete_view')
    )


def password_reset_done(request):
    return django_password_reset_done(request, template_name='commons/password_reset_done.html')


def password_reset_complete(request):
    return django_password_reset_complete(request, template_name='commons/password_reset_complete.html')


@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request):
    if not request.user.has_usable_password():
        # only standard users can change password
        return HttpResponseRedirect('/')
    else:
        return django_password_change(
            request,
            template_name='commons/password_change_form.html',
            post_change_redirect=reverse('commons.views.password_change_done'),
            password_change_form=PasswordChangeForm,
            current_app=None,
            extra_context=None
        )


@login_required
def password_change_done(request):
    return django_password_change_done(
        request,
        template_name='commons/password_change_done.html',
        current_app=None,
        extra_context=None
    )


@login_required
def password_set(request):
    if request.user.has_usable_password():
        # only standard users can't set password
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, data=request.POST)
            if form.is_valid():
                form.save()
        else:
            form = SetPasswordForm(request.user)

        return render_to_response(
            'commons/password_set_form.html',
            {'form': form, 'user': request.user},
            context_instance=RequestContext(request)
        )
