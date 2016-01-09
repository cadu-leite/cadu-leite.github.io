#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Carlos Leite'
SITENAME = u'cadu-leite'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

THEME = 'theme'

GOOGLE_ANALYTICS = 'UA-72223300-1'
GITHUB_URL = 'https://github.com/cadu-leite'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('ZNC Sistemas', 'http://znc.com.br'),
    ('PythonPeople', 'http://people.python.org.br/'),
    ('Python.org', 'http://python.org/'),
    ('Pelican', 'http://getpelican.com/'),
    )

SOCIAL = (('bitbucket', 'https://bitbucket.org/carlos_leite/'),
          ('github', 'https://github.com/cadu-leite'),
          ('g+', 'https://google.com/+CarlosLeite'),
          ('linkedin', 'https://br.linkedin.com/in/carlosleite/en'),
          ('rss', '//blog.alexandrevicenzi.com/feeds/all.atom.xml'))


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#CUSTOM Booystrap3 settings
# the Bootstrap3 theme has benn customized.
# Settings VARS name didnt, but the behavior slightly diff
HIDE_SIDEBAR = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = False