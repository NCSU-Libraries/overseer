"""
overseer.context_processors
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2011 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""

from django.core.urlresolvers import reverse

import overseer
from overseer import conf

def default(request):
    return {
        'request': request,
        'OVERSEER_TITLE': conf.TITLE,
        'OVERSEER_NAME': conf.NAME,
        'OVERSEER_VERSION': overseer.VERSION,
        'OVERSEER_ALLOW_SUBSCRIPTIONS': conf.ALLOW_SUBSCRIPTIONS,
        'HOMEPAGE_RELOAD': conf.HOMEPAGE_RELOAD,
        'HOMEPAGE_RELOAD_DELAY_MS': conf.HOMEPAGE_RELOAD_DELAY_MS,
    }
