--------
Overseer
--------

This is an updated, and reskinned for of the original Overseer project.  Overseer is a simple status board app written in Django.

Configuration options
---------------------

TITLE
  The title for your page
  
NAME
  The heading text for your page
  
MEDIA_PREFIX
  The prefix for overseer's media -- by default this is handled using Django's static media server (pre-1.3)
  
BASE_URL
  the base url to overseer

HOMEPAGE_RELOAD
  Reload homepage at an interval. It's ignored if GET parameter AutoReload=True is set
  
HOMEPAGE_RELOAD_DELAY_MS
  Interval for reloading homepage (in milliseconds)
