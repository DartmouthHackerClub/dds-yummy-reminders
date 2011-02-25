from django.conf.urls.defaults import *

urlpatterns = patterns('scrape.dds.views',
    (r'^istheregeneraltsos$', 'generaltso'),
    (r'^lookfor$', 'lookfor'),
    (r'^subscribe$', 'subscribe'),
    (r'^unsubscribe/(?P<email>.+)/(?P<id>\d+)/$', 'unsubscribe'),
)
