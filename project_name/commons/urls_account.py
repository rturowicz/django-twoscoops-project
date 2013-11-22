from django.conf.urls import *


urlpatterns = patterns(
    'commons.views',
    url(r'^login/$', 'login', {}, 'login_view'),
    url(r'^logout/$', 'logout', {}, name="logout_view"),
    url(r'^password/set/$', 'password_set', name='password_set_view'),
    url(r'^password_reset/$', 'password_reset', name='password_reset_view'),
    url(r'^reset/done/$', 'password_reset_complete', name='password_reset_complete_view'),
    url(r'^password_reset/done/$', 'password_reset_done', name='password_reset_done_view'),
    url(
        r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'password_reset_confirm',
        name='password_reset_confirm_view'
    ),
    url(r'^password/change/$', 'password_change', name='password_change_view'),
    url(r'^password/change/done/$', 'password_change_done', name='password_change_done_view'),
)
