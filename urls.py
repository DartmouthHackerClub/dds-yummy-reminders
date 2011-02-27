from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
#    (r'^dds/admin/doc/', include('django.contrib.admindocs.urls')),

    #(r'^dds/', 'scrape.dds.views.subscribe'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Example:
    (r'^app/', include('scrape.dds.urls')),
)
