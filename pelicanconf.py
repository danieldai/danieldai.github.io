#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel Dai'
SITETITLE = 'Daniel Dai'
SITENAME = u"Daniel Dai's Blog"
SITEURL = 'http://localhost:8000'

OUTPUT_PATH = 'docs/'
PATH = 'content'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = 'zh'

COPYRIGHT_YEAR = "2021"
COPYRIGHT_NAME = 'Daniel Dai'

CC_LICENSE = {
    "name": "自由转载-非商用-非衍生-保持署名",
    "version": "3.0",
    "slug": "by-nc-nd",
    "language": "zh"
}

MAIN_MENU = True

LINKS = (
#     ("Linkedin", "https://www.linkedin.com/in/daniel-dai/"),
#     ("Github", "https://github.com/danieldai"),
)

SOCIAL = (
    ("github", "https://github.com/danieldai"),
    ("linkedin", "https://www.linkedin.com/in/daniel-dai"),
    ("twitter", "https://x.com/_DanielDai_"),
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

SITESUBTITLE = "人工智能和互联网"

LOAD_CONTENT_CACHE = False

DISPLAY_PAGES_ON_MENU = True

# SITEIMAGE = '/daniel_150.jpeg'

THEME_CSS_OVERRIDES = ['theme/css/oldstyle.css']

SITE_SUBTEXT = "Day after day, we are closer to the Matrix, it's IT."

META_DESCRIPTION = """
Daniel Dai is an Experienced Software Professional in Python, Java and Web, who has 
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

PLUGIN_PATHS = ['../pelican-plugins']
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
