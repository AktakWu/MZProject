#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""

from django.conf.urls import patterns, url
from common import views
from django.conf import settings
import django

urlpatterns = patterns('common.views',
    url(r'^$', views.index, name='index'),
    url(r'^header/$', views.aaa),
    url(r'^uploads/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT,'show_indexes':True}),

    url(r'^common/search/$',views.keywords_search),#ajax keywords
    url(r'^login/$',views.login),
    url(r'^teacher/$',views.teacher ),

)
