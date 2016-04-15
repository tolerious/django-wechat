# -*- coding: utf-8 -*-
'''
Created on 04 15, 2016

@author: tolerious

'''

from django_weixin.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_weixin.ierror import *
from django_weixin.api_errors import *
import logging, json


