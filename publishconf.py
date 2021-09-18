#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.danieldai.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

DISQUS_SITENAME = "danieldai"
GOOGLE_ANALYTICS = "UA-72604787-1"
GITHUB_URL = "https://github.com/danieldai"
GOOGLE_ANALYTICS_ID = GOOGLE_ANALYTICS # for alchemy theme

GOOGLE_GLOBAL_SITE_TAG = 'G-286858962'

# GOOGLE_ADSENSE = {
#     'ca_id': 'ca-pub-1234567890',    # Your AdSense ID
#     'page_level_ads': True,          # Allow Page Level Ads (mobile)
#     'ads': {
#         'aside': '1234561',          # Side bar banner (all pages)
#         'main_menu': '1234562',      # Banner before main menu (all pages)
#         'index_top': '1234563',      # Banner after main menu (index only)
#         'index_bottom': '1234564',   # Banner before footer (index only)
#         'article_top': '1234565',    # Banner after article title (article only)
#         'article_bottom': '1234566', # Banner after article content (article only)
#     }
# }