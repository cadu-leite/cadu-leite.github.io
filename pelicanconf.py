#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Carlos Leite'
SITENAME = u'cadu-leite'
SITEURL = ''
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'
THEME = 'theme'
DEFAULT_PAGINATION = 5


PATH = 'content'


GOOGLE_ANALYTICS = 'UA-72223300-1'
GITHUB_URL = 'https://github.com/cadu-leite'

# FEEDs
FEED_USE_SUMMARY = True

FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'


# Blogroll
LINKS = (
    ('ZNC Sistemas', 'http://znc.com.br'),
    ('PythonPeople', 'http://people.python.org.br/'),
    ('Python.org', 'http://python.org/'),
    ('Pelican', 'http://getpelican.com/'),
    )

SOCIAL = (
    ('twitter', 'https://twitter.com/cadu_leite'),

    ('bitbucket', 'https://bitbucket.org/carlos_leite/'),
    ('github', 'https://github.com/cadu-leite'),
    ('google-plus', 'https://google.com/+CarlosLeite'),
    ('linkedin', 'https://br.linkedin.com/in/carlosleite/en'),
    ('rss', 'http://cadu-leite.github.io/feeds/all.atom.xml'),
    ('twitter PythonPeople', 'https://twitter.com/pythonpeople'),

)


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# CUSTOM Booystrap3 settings
# the Bootstrap3 theme has benn customized.
# Settings VARS name didnt, but the behavior slightly diff

BOOTSTRAP_NAVBAR_INVERSE = False
HIDE_SIDEBAR = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = False
