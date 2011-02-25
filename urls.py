from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^scrape/dds/', include('scrape.dds.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^scrape/admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^scrape/admin/', include(admin.site.urls)),
)
