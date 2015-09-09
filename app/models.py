from django.db import models
import requests, logging
from wechat_server import *
# Create your models here.

class AccessToken(models.Model):
    corpid = models.CharField(default='corpid', max_length=200)
    corpsecret = models.CharField(default='corpsecret', max_length=200)
    token = models.CharField(default='abc', max_length=500)
    aeskey = models.CharField(default='abc', max_length=1000)

    def __unicode__(self):
        return self.corpid + ";" + self.corpsecret

    def get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+ self.corpid+'&corpsecret=' + self.corpsecret
        r = requests.get(url, verify=False)
        try:
            access_token = r.json()['access_token']
            return access_token
        except Exception as e:
            logging.info(str(e))
            return 'Invalidate'