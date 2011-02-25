from django.conf.urls.defaults import *
from scrape.dds.models import Profile

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^scrape/accounts/register$', 'registration.views.register'),
    (r'^scrape/accounts/', include('registration.urls')),
    (r'^scrape/dds/', include('scrape.dds.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^scrape/admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^scrape/admin/', include(admin.site.urls)),
)
