from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('views',
    # Examples:
    # url(r'^$', 'twoacl.views.home', name='home'),
    url(r'^/tweet/$', tweet),
    url(r'^/seek-permission/$', seek_permission),
    url(r'^/permission-obtained/$', permission_obtained),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
