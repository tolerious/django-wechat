# -*- coding: utf-8 -*-
'''
Created on 04 11, 2016

@author: tolerious

'''

from django_weixin.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_weixin.ierror import *


def create_menu_admin(request):
    return render(request,'menu_config.html')

def create_basic_menu(request):
    pass
