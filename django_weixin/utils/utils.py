# -*- coding: utf-8 -*-
'''
Created on 04 08, 2016

@author: tolerious

'''
import datetime, requests, json
import json, xml.etree.ElementTree as et
from django_weixin.WXBizMsgCrypt import *


def python_time_to_javascript(python_datetime):
    if python_datetime is not None:
        if type(python_datetime) == type(datetime.date.today()):
            python_datetime = datetime.datetime.combine(python_datetime, datetime.time())
        javascript_time = (python_datetime - datetime.datetime.utcfromtimestamp(0)).total_seconds()
        javascript_time = int(javascript_time * 1000)
        return javascript_time
    else:
        return 0


def javascript_time_to_python_datetime(javascript_time):
    python_datetime = datetime.datetime.utcfromtimestamp(javascript_time / 1000.0)
    return python_datetime


def get_xml_text_by_property(xml_string, property):
    root = et.fromstring(xml_string)
    for want_string in root.iter(property):
        return want_string.text


def judge_message_is_valid(access_token, aeskey, corpid, signature, timestamp, nonce, echostr):
    wx = WXBizMsgCrypt(access_token, aeskey, corpid)
    ret, return_token = wx.VerifyURL(signature, timestamp, nonce, echostr)
    return ret, return_token  # if ret == 0, valid


def generate_create_base_menu_button_json():  # 生成基础功能的button,click,view类型的button
    base_json = {
        "button": []
    }
    return base_json


def get_follower_info():
    from django_weixin.models.basic import *
    url = """https://api.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&next_openid="""
    a = AccessToken.objects.get(pk=1)
    access_token = a.get_access_token()
    new_url = url.format(access_token=access_token)
    print new_url
    r = requests.get(new_url)
    print r.json()
