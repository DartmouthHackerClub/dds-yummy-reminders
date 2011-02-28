from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    (r'^istheregeneraltsos$', 'scrape.dds.views.generaltso'),
    (r'^lookfor$', 'scrape.dds.views.lookfor'),
    (r'^subscribe$', 'scrape.dds.views.subscribe'),
    (r'^$', 'scrape.dds.views.subscribe'),
    (r'^unsubscribe/(?P<email>.+)/(?P<tag>.+)/$', 'scrape.dds.views.unsubscribe'),
    (r'^unsubscribe_all/(?P<email>.+)/(?P<tag>.+)/$', 'scrape.dds.views.unsubscribe_all'),


#    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),

)
