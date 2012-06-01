from django.conf.urls import patterns, include, url
import whitelist.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mentoringmatch.views.home', name='home'),
    # url(r'^mentoringmatch/', include('mentoringmatch.foo.urls')),
    url(r'^$', 'whitelist.views.login'),
    url(r'^login/', 'whitelist.views.login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
