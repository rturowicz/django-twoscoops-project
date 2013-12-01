from django.conf.urls import *


urlpatterns = patterns(
    'profiles.views',
    url(r'^$', 'index', {}, 'profile_view'),
    url(r'^(?P<user_id>\d+)/$', 'user', {}, 'user_view'),
)
