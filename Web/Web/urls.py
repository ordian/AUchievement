from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'Achievement.views.dashboard', name='dashboard'),
    url(r'^achievements/?$', 'Achievement.views.achievements', name='achievements'),
    url(r'^people/?$', 'Achievement.views.people', name='people'),
    url(r'^statistics/?$', 'Achievement.views.statistics', name='statistics'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^achievement/new/?', 'Achievement.views.new_achievement', name='new_achievement'),
    url(r'^achievement/view/?', 'Achievement.views.view_achievements', name='view_achievement'),
)
