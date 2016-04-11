# -*- coding: utf-8 -*-
'''
Created on 04 08, 2016

@author: tolerious

'''


from django.db import models
import requests, logging, uuid

def convert_uuid_to_string():
    return str(uuid.uuid4())

class TopLevelMenu(models.Model):
    type = models.CharField(max_length=10,default="click")
    name = models.CharField(max_length=50,default="test")
    key = models.CharField(max_length=100,default=convert_uuid_to_string)
    url = models.CharField(max_length=1000,default="")
    sub_menu = models.CharField(max_length=1000,null=True)







