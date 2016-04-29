from django.db import models
import requests, logging
import datetime, pytz
from wechat_server import *
from django_weixin.utils.utils import *
from django.conf import settings


# Create your models here.

class AccessToken(models.Model):
    corpid = models.CharField(default=settings.APP_ID, max_length=200)
    corpsecret = models.CharField(default=settings.APP_SECRET, max_length=200)
    token = models.CharField(default=settings.WX_TOKEN, max_length=1000)
    aeskey = models.CharField(default=settings.AES_KEY, max_length=1000)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    accesstoken = models.CharField(default="", max_length=500)

    def __unicode__(self):
        return self.corpid + ";" + self.corpsecret

    def get_access_token(self):
        timedel = datetime.datetime.now() - self.create_time.replace(tzinfo=None)
        if timedel.seconds > 2 * 60 * 60 or self.accesstoken == "":
            url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + settings.APP_ID + '&secret=' + settings.APP_SECRET
            r = requests.get(url, verify=False)
            try:
                logging.info(r.json())
                access_token = r.json()['access_token']
                self.accesstoken = access_token
                self.create_time = datetime.datetime.now()
                self.save()
                return access_token
            except Exception as e:
                logging.info(str(e))
                return 'Invalidate'
        else:
            return self.accesstoken

    @classmethod
    def get_wechat_server_ip_list(cls, token):
        url = "https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=" + token
        r = requests.get(url, verify=False)
        try:
            ip_list = r.json()['ip_list']
            logging.info(ip_list)
            logging.info(type(ip_list))
            return ip_list
        except Exception as e:
            logging.info(str(e))
            return []


class BasicMessage(models.Model):
    to_user_name = models.CharField(default="", max_length=500)
    from_user_name = models.CharField(default="", max_length=500)
    create_time = models.CharField(default="", max_length=500)
    message_type = models.CharField(default="", max_length=500)
    message_id = models.CharField(default="", max_length=1000)

    def __unicode__(self):
        return "[from_user_name]:" + self.from_user_name + ", [message_type]:" + self.message_type


class TextMessage(BasicMessage):
    TextMessageTemplate = u"""<xml>
<ToUserName><![CDATA[{toUser}]]></ToUserName>
<FromUserName><![CDATA[{fromUser}]]></FromUserName>
<CreateTime>{create_time}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{message_content}]]></Content>
</xml>
    """
    message_content = models.TextField(default="")

    def __unicode__(self):
        return "[message type]:" + self.message_type + "; [message content]:" + self.message_content


class KeFuMessage(BasicMessage):
    KeFuMessageTemplate = u"""<xml>
<ToUserName><![CDATA[{toUser}]]></ToUserName>
<FromUserName><![CDATA[{fromUser}]]></FromUserName>
<CreateTime>{create_time}</CreateTime>
<MsgType><![CDATA[transfer_customer_service]]></MsgType>
<Content><![CDATA[{message_content}]]></Content>
</xml>
    """
    message_content = models.TextField(default="")

    def __unicode__(self):
        return "[message type]:" + self.message_type + "; [message content]:" + self.message_content


class PicMessage(BasicMessage):
    pic_url = models.CharField(default="", max_length=1000)
    media_id = models.CharField(default="", max_length=1000)

    def __unicode__(self):
        pass  # todo


class VoiceMessage(BasicMessage):
    media_id = models.CharField(default="", max_length=1000)
    format = models.CharField(default="", max_length=20)

    def __unicode__(self):
        pass  # todo


class VideoMessage(BasicMessage):
    media_id = models.CharField(default="", max_length=1000)
    thumb_media_id = models.CharField(default="", max_length=1000)

    def __unicode__(self):
        pass  # todo


class SmallVideoMessage(BasicMessage):
    media_id = models.CharField(default="", max_length=1000)
    thumb_media_id = models.CharField(default="", max_length=1000)

    def __unicode__(self):
        pass  # todo


class LocationMessage(BasicMessage):
    location_x = models.CharField(default="", max_length=1000)
    location_y = models.CharField(default="", max_length=1000)
    scale = models.CharField(default="", max_length=500)
    label = models.CharField(default="", max_length=1000)

    def __unicode__(self):
        pass  # todo


class LinkMessage(BasicMessage):
    title = models.CharField(default="", max_length=1000)
    description = models.CharField(default="", max_length=1000)
    url = models.CharField(default="", max_length=1000)

    def __unicode__(self):
        pass  # todo


class BasicEvent(models.Model):
    to_user_name = models.CharField(default="", max_length=500)
    from_user_name = models.CharField(default="", max_length=500)
    create_time = models.CharField(default="", max_length=500)
    message_type = models.CharField(default="", max_length=500)
    event = models.CharField(default="", max_length=30)

    def __unicode__(self):
        pass  # todo


# class SubscribeEvent(BasicEvent):
#
#     def __unicode__(self):
#         pass # todo


class ScanQRcodeEvent(BasicEvent):
    event_key = models.CharField(default="", max_length=500)
    ticket = models.CharField(default="", max_length=500)

    def __unicode__(self):
        pass  # todo


class LocationEvent(BasicEvent):
    latitude = models.CharField(default="", max_length=500)
    longitude = models.CharField(default="", max_length=500)
    precision = models.CharField(default="", max_length=500)

    def __unicode__(self):
        pass  # todo


class MenuEvent(BasicEvent):
    event_key = models.CharField(default="", max_length=500)

    def __unicode__(self):
        pass  # todo


class MessageAutoReplay(models.Model):
    content = models.CharField(max_length=500, default="")
    create_time = models.DateTimeField(default=datetime.datetime.now, auto_now=datetime.datetime.now)

    def __unicode__(self):
        return self.content + "\n"
