# -*- coding: utf-8 -*-
import os
from urllib.parse import urlparse

DEBUG = True
SECRET_KEY = b'hello 42'

from os.path import dirname, abspath, join
SQLALCHEMY_ECHO = True

default_db = 'sqlite:////%s/data.sqlite' % dirname(abspath(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default_db)

# flatpages
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = join(dirname(__file__), 'docs')

# default babel values
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'
ACCEPT_LANGUAGES = ['en', 'ru', ]

# available languages
LANGUAGES = {
    'en': u'English',
    'uk': u'Українська'
}

# make sure that you have started debug mail server using command
# $ make mail
MAIL_SERVER = 'localhost'
MAIL_PORT = 20025
MAIL_USE_SSL = False
MAIL_USERNAME = 'your@email.address'
#MAIL_PASSWORD = 'topsecret'

# Celery
BROKER_TRANSPORT = 'redis'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_DISABLE_RATE_LIMITS = True
CELERY_ACCEPT_CONTENT = ['json',]

# cache
CACHE_TYPE = 'redis'
CACHE_KEY_PREFIX = 'eventsmonkey'

CACHE_REDIS_HOST = 'localhost',
CACHE_REDIS_PORT = 6379
CACHE_REDIS_URL = 'redis://127.0.0.1:6379'
CACHE_REDIS_DB = 1

# Auth
SESSION_COOKIE_NAME = 'session'

SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/auth/loggedin'
SOCIAL_AUTH_USER_MODEL = 'admin_service.models.User'
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',
)

# Documnetation http://psa.matiasaguirre.net/docs/backends/index.html
# https://github.com/settings/applications/
SOCIAL_AUTH_GITHUB_KEY = '8b643b3f60a3dd4470e7'
SOCIAL_AUTH_GITHUB_SECRET = '3e07a41b69244ec209db690e1babab3ca1d33291'
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']

default_events_service = 'http://127.0.0.1:5000'
EVENTS_SERVICE_URL = os.environ.get('EVENTS_SERVICE_URL',
                                    default_events_service)

del dirname, abspath, join, urlparse, os
