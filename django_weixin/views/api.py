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
                        "name": "我的订单",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx73cedfdd4ac51d80&redirect_uri=http%3a%2f%2fwx.meiparking.com%2fwechat%2forder%2flist%3fcurrent%3d1&response_type=code&scope=snsapi_base#wechat_redirect"
                    },
                    {
                        "type": "view",
                        "name": "预约服务",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx73cedfdd4ac51d80&redirect_uri=http%3a%2f%2fwx.meiparking.com%2fwechat%2freserve%2fpark%2f&response_type=code&scope=snsapi_base#wechat_redirect"
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
                    {
                        "type": "view",
                        "name": "操作流程",
                        "url": "http://a.app.qq.com/o/simple.jsp?pkgname=com.meiparking.meiparkingclient"
                    },
                    {
                        "type": "view",
                        "name": "操作流程",
                        "url": "http://a.app.qq.com/o/simple.jsp?pkgname=com.meiparking.meiparkingclient"
                    }
                ]
            }
        ]
    }
    whole_menu_dic =  {
     "button":[
     {
          "type":"click",
          "name":u"你好",
          "key":"V1001_TODAY_MUSIC"
      },
      {
           "name":u"asdf",
           "sub_button":[
           {
               "type":"view",
               "name":u"sdf",
               "url":"http://www.soso.com/"
            },
            {
               "type":"view",
               "name":u"asdf",
               "url":"http://v.qq.com/"
            },
            {
               "type":"click",
               "name":u"asdf",
               "key":"V1001_GOOD"
            }]
       }]
 }
    token_obj = AccessToken.objects.get(pk=1)
    token = token_obj.get_access_token()
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + token
    payload = whole_menu_dic
    logging.info(payload)
    r = requests.post(url, data=json.dumps(payload,ensure_ascii=False))
    logging.info(r.text)
    logging.info(r.json())
    return Http200(request)
