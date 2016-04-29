__author__ = 'tolerious'
from django.conf.urls import patterns, url

from django_weixin.views import basic, menu, api

urlpatterns = patterns('',
                       url(r'^validate/', basic.index, name='index'),
                       # url(r'^token/$', basic.accesstoken, name='accesstoken'),
                       url(r'^menu/config/', menu.create_menu_admin, name='menu_admin_page'),
                       url(r'^basic/menu/create/', menu.create_basic_menu, name='create_basic_menu'),
                       url(r'^access/token/get/', basic.get_access_token_view, name='get_access_token_view'),
                       url(r'^admin/dashboard/', basic.admin_dashboard, name='admin_dashboard'),
                       url(r'^show/ticket/', basic.get_qr_code_ticket, name='get_temp_qr_code'),

                       url(r'^api/create/menu/', api.create_meibo_menu, name='create_meibo_menu'),
                       url(r'^api/delete/menu', api.delete_menu, name="delete_meibo_menu"),
                       )
