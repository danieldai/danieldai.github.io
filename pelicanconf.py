#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel Dai'
SITENAME = u'Daniel Dai - Python, Java and Web'
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
                'extra/daniel_150.jpeg' 
                ]
                
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                        'extra/daniel_150.jpeg': {'path': 'daniel_150.jpeg'}}

SITESUBTITLE = "Daniel Dai - Web Tech Professional"

LOAD_CONTENT_CACHE = False

DISPLAY_PAGES_ON_MENU = True

PROFILE_IMAGE = '/daniel_150.jpeg'

SITE_SUBTEXT = "Day after day, we are closer to the Matrix, it's IT."

META_DESCRIPTION = """
Daniel Dai(代明) is an Experienced Software Professional in Python, Java and Web, who has 
passionate enthusiasm in changing people's life with Information Tech in various aspects. 
"""

PAGES_ON_MENU = True
CATEGORIES_ON_MENU = True
TAGS_ON_MENU = True
ARCHIVES_ON_MENU = True

EMAIL_ADDRESS = 'daeming@gmail.com'
GITHUB_ADDRESS = 'https://github.com/danieldai'
SO_ADDRESS = 'http://stackoverflow.com/users/1089262/daniel-dai'

PLUGIN_PATHS = ['/home/daniel/github/pelican-plugins']

PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
