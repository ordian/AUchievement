from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'Achievement.views.dashboard', name='dashboard'),
    url(r'^people/?$', 'Achievement.views.people', name='people'),
    url(r'^statistics/id/(?P<id>[0-9]+)$', 'Achievement.views.statistics', name='statistics'),
    url(r'^achievements/id/(?P<id>[0-9]+)$', 'Achievement.views.achievements', name='achievements'),

    url(r'^admin/', include(admin.site.urls)),
)
