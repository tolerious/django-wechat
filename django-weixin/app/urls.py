__author__ = 'tolerious'
from django.conf.urls import patterns, url

from app.views import basic

urlpatterns = patterns('',
                       url(r'^validate/', basic.index, name='index'),
                       url(r'^token/$', basic.accesstoken, name='accesstoken'),
                       )
