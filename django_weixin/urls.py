__author__ = 'tolerious'
from django.conf.urls import patterns, url

from django_weixin.views import basic, menu, api

urlpatterns = patterns('',
                       url(r'^validate/', basic.index, name='index'),
                       # url(r'^token/$', basic.accesstoken, name='accesstoken'),
                       url(r'^menu/config/', menu.create_menu_admin, name='menu_admin_page'),
                       url(r'^basic/menu/create/', menu.create_basic_menu, name='create_basic_menu'),
                       url(r'^access/token/get/', basic.get_access_token_view, name='get_access_token_view'),
                       )
