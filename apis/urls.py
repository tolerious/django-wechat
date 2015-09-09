'''
Created on 03 21, 2015

@author: tolerious

'''
from django.conf.urls import patterns, url
from apis import address_book

urlpatterns = patterns('',
        # address book APIs
    url(r'^%s%s'   %('create/','department/'),     address_book.create_department, name='api_create_department'),


        )