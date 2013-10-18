"""
overseer.urls
~~~~~~~~~~~~~

:copyright: (c) 2011 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""

from django.conf.urls.defaults import *
from django.views.generic.base import RedirectView
import os.path

urlpatterns = patterns('',
    url(r'^$', 'overseer.views.index', name='index'),
    url(r'^service/(?P<slug>[^/]+)/$', 'overseer.views.service', name='service'),
    url(r'^service/(?P<slug>[^/]+)/last-event/$', 'overseer.views.last_event', name='last_event'),
    url(r'^event/(?P<id>[^/]+)/$', 'overseer.views.event', name='event'),
    url(r'^(?P<id>\d+)$', RedirectView.as_view(url='event/%(id)s/'), name='event_short'),
    url(r'^subscribe/$', 'overseer.views.create_subscription', name='create_subscription'),
    url(r'^subscription/(?P<ident>[^/]+)/$', 'overseer.views.update_subscription', name='update_subscription'),
    url(r'^subscription/(?P<ident>[^/]+)/verify/$', 'overseer.views.verify_subscription', name='verify_subscription'),
)
