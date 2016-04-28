'''
Created on 03 19, 2015

@author: tolerious

'''
from django.db import models
import requests, logging

class WeChatServer(models.Model):
    server_ip_list = models.CharField(default="",blank=True,max_length=1000)

    def get_wechat_server_ip_list(self):
        from django_weixin.models.basic import *
        access_token = AccessToken.objects.get(id=1)
        token = access_token.get_access_token()
        url = "https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=" + token
        r = requests.get(url, verify=False)
        try:
            ip_list = r.json()['ip_list']
            str = ""
            for i in ip_list:
                temp_i = i + ","
                str += temp_i
            self.server_ip_list = str
            return ip_list
        except Exception as e:
            return ""
            logging.info(str(e))
