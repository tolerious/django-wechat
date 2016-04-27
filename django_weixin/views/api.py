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
import logging, json, requests


@csrf_exempt
def create_meibo_menu(request):
    whole_menu_dic = {
        "button": [
            {
                "name": "泊/取车",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "预约服务",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx73cedfdd4ac51d80&redirect_uri=http%3a%2f%2fwx.meiparking.com%2fwechat%2freserve%2fpark%2f&response_type=code&scope=snsapi_base#wechat_redirect"
                    },
                    {
                        "type": "view",
                        "name": "我的订单",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx73cedfdd4ac51d80&redirect_uri=http%3a%2f%2fwx.meiparking.com%2fwechat%2forder%2flist%3fcurrent%3d1&response_type=code&scope=snsapi_base#wechat_redirect"
                    }
                ]
            },
            {
                "name": "个人中心",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "我的美泊",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx73cedfdd4ac51d80&redirect_uri=http%3a%2f%2fwx.meiparking.com%2fwechat%2fpersonal%2fcenter%2f&response_type=code&scope=snsapi_base#wechat_redirect"
                    },
                    {
                        "type": "view",
                        "name": "分享领红包",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx73cedfdd4ac51d80&redirect_uri=http%3a%2f%2fwx.meiparking.com%2fwechat%2fsharing%2fbonus%2f&response_type=code&scope=snsapi_base#wechat_redirect"
                    },
                    {
                        "type": "view",
                        "name": "新分享",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx73cedfdd4ac51d80&redirect_uri=http%3a%2f%2fwx.meiparking.com%2fwechat%2fmarket%2fh5%2f&response_type=code&scope=snsapi_base#wechat_redirect"
                    }
                ]
            },
            {
                "name": "更多",
                "sub_button": [
                    # {
                    #     "type": "view",
                    #     "name": "操作流程",
                    #     "url": "http://a.app.qq.com/o/simple.jsp?pkgname=com.meiparking.meiparkingclient"
                    # },
                    # {
                    #     "type": "view",
                    #     "name": "操作流程",
                    #     "url": "http://a.app.qq.com/o/simple.jsp?pkgname=com.meiparking.meiparkingclient"
                    # },
                    {
                        "type": "scancode_waitmsg",
                        "name": "扫码显示",
                        "key": "myscancode",
                        "sub_button": []
                    },
                    {
                        "type": "scancode_push",
                        "name": "扫码跳转",
                        "key": "myscancodepush",
                        "sub_button": []
                    },
                    {
                        "type": "pic_photo_or_album",
                        "name": "拍照",
                        "key": "rselfmenu_1_1",
                        "sub_button": []
                    },
                ]
            }
        ]
    }
    token_obj = AccessToken.objects.get(pk=1)
    token = token_obj.get_access_token()
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + token
    payload = whole_menu_dic
    # logging.info(payload)
    r = requests.post(url, data=json.dumps(payload, ensure_ascii=False))
    logging.info(r.json())
    return_data = r.json()
    if return_data['errmsg'] == "ok":
        logging.info("菜单创建成功.")
        return Http200(request)
    else:
        return Http400(request)


@csrf_exempt
def delete_menu(request):
    token_obj = AccessToken.objects.get(pk=1)
    token = token_obj.get_access_token()
    url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=" + token
    r = requests.get(url)
    logging.info(r.json())
    if r.json()['errmsg'] == "ok":
        logging.info("菜单删除成功.")
        return Http200(request)
    else:
        return Http400(request)
