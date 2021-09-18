#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel Dai'
SITETITLE = 'Daniel Dai'
SITENAME = u'Daniel Dai的网络日志'
SITEURL = 'https://www.danieldai.com'

PATH = 'content'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = 'zh'

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

MAIN_MENU = True

LINKS = (
#     ("Linkedin", "https://www.linkedin.com/in/daniel-dai/"),
#     ("Github", "https://github.com/danieldai"),
)

SOCIAL = (
    ("github", "https://github.com/danieldai"),
    ("linkedin", "https://www.linkedin.com/in/daniel-dai"),
    ("twitter", "https://twitter.com/danieldai_com"),
)

MENUITEMS = (
    ("存档", "/archives.html"),
    ("分类", "/categories.html"),
    ("标签", "/tags.html"),
)

PYGMENTS_STYLE = "github"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "themes/Flex"
EXTRA_FAVICON = True

# Blogroll
FOOTER_LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

ICONS = (
    ('github', 'https://github.com/danieldai'),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 
                'extra/CNAME',
                'extra/daniel_150.jpeg' 
                ]
                
SITELOGO = SITEURL + "/daniel_150.jpeg"

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                        'extra/daniel_150.jpeg': {'path': 'daniel_150.jpeg'}}

SITESUBTITLE = "互联网产品和技术"

LOAD_CONTENT_CACHE = False

DISPLAY_PAGES_ON_MENU = True

# SITEIMAGE = '/daniel_150.jpeg'

THEME_CSS_OVERRIDES = ['theme/css/oldstyle.css']

SITE_SUBTEXT = "Day after day, we are closer to the Matrix, it's IT."

META_DESCRIPTION = """
Daniel Dai(代明) is an Experienced Software Professional in Python, Java and Web, who has 
passionate enthusiasm in changing people's life with Information Tech in various aspects. 
"""

PAGES_ON_MENU = True
CATEGORIES_ON_MENU = True
TAGS_ON_MENU = True
ARCHIVES_ON_MENU = True
HIDE_AUTHORS = True

DEFAULT_DATE_FORMAT = '%Y年%m月%d日'

EMAIL_ADDRESS = 'daeming@gmail.com'
GITHUB_ADDRESS = 'https://github.com/danieldai'
SO_ADDRESS = 'http://stackoverflow.com/users/1089262/daniel-dai'

PLUGIN_PATHS = ['/home/daniel/danieldai/pelican-plugins']

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
