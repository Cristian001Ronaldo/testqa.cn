#!/usr/bin/env python
# encoding: utf-8
__author__ = 'xwchen2'
from django.conf.urls import patterns, url

urlpatterns = patterns('article.views',
    url(r'^$', 'home'),
    url(r'^article$', 'article'),
)