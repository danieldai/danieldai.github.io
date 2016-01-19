#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel Dai'
SITENAME = u'Daniel Dai - An Engineer'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "themes/alchemy"
EXTRA_FAVICON = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Gather Health', 'https://gatherhealth.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 
                'extra/CNAME',
                'extra/daniel.jpeg' 
                ]
                
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                        'extra/daniel.jpeg': {'path': 'daniel.jpeg'}}

SITESUBTITLE = "Day after day, we are closer to the Matrix, it's IT."

LOAD_CONTENT_CACHE = False

DISPLAY_PAGES_ON_MENU = True

PROFILE_IMAGE = '/daniel.jpeg'

SITE_SUBTEXT = SITESUBTITLE