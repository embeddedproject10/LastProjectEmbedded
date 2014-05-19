from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lastProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^update/(?P<place>\w{0,30})/(?P<direction>\w{0,30})/(?P<statue>\w{0,30})/$', 'myapp.views.update'),
    url(r'^view/$', 'myapp.views.view'),
)
