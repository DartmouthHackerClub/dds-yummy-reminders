from django.conf.urls.defaults import *

urlpatterns = patterns('scrape.dds.views',
    (r'^istheregeneraltsos$', 'generaltso'),
    (r'^lookfor$', 'lookfor'),
    (r'^subscriptions$', 'subscriptions'),
)
