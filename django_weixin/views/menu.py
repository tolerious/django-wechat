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
from django_weixin.api_errors import *
import logging, json


def create_menu_admin(request):
    return render(request, 'menu_config.html')

@csrf_exempt
def create_basic_menu(request):
    if request.method == "POST":
        data = json.loads(request.body)
        logging.info(data)
        menu_1_list = data['menu_1']
        menu_2_list = data['menu_2']
        menu_3_list = data['menu_3']
        if menu_1_list[0]['menu_type'] == "click" or menu_1_list[0]['menu_type'] == "view" or menu_1_list[0]['menu_type'] == "0":  # 说明是没有子菜单的
            if menu_1_list[0]['menu_type'] == '0':
                pass
            else:
                if menu_1_list[0]['menu_type'] == 'click':
                    pass
        if menu_2_list[0]['menu_type'] == "click" or menu_2_list[0]['menu_type'] == "view" or menu_2_list[0]['menu_type'] == "0":  # 说明是没有子菜单的
            pass
        if menu_3_list[0]['menu_type'] == "click" or menu_3_list[0]['menu_type'] == "view" or menu_3_list[0]['menu_type'] == "0":  # 说明是没有子菜单的
            pass
        return Http200(request)
    else:
        return Http400(request)
