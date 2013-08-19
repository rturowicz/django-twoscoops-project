from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib import admin


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
    # debug-toolbar-user-panel
    url(r'', include('debug_toolbar_user_panel.urls')),

    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

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
