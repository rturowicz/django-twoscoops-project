from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib import admin

from commons import urls_account
from profiles import urls_registration

#info_dict = {
#    'queryset': Entry.objects.all(),
#    'date_field': 'pub_date',
#}

sitemaps = {
    'flatpages': FlatPageSitemap,
    # 'entry': GenericSitemap(info_dict, priority=0.6),
}

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'django_template_15.views.home', name='home'),
    # url(r'^django_template_15/', include('django_template_15.foo.urls')),

    # profiles (login, logout, etc.)
    url(r'^accounts/', include(urls_account)),

    # simple captcha
    url(r'^captcha/', include('captcha.urls')),

    # account registration and confirmation
    url(r'^registration/', include(urls_registration)),

    # profile
    url(r'^profiles/', include('profiles.urls')),

    # sitemap & robots
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, 'sitemap_xml'),
    url(r'^robots\.txt$', 'commons.views.robots', {}, 'robots_txt'),

    # django-rosetta
    url(r'^rosetta/', include('rosetta.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        #url(r'^testing/', include('testing.urls')),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

    # Uncomment the next line to serve media files in dev.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
