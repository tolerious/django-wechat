from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import logging
from models import AccessToken
from WXBizMsgCrypt import *
logger = logging.getLogger('wechat')
# Create your views here.

def index(request):
    atoken = AccessToken.objects.get(id=1)
    corpid = atoken.corpid
    aeskey = atoken.aeskey
    token = atoken.token
    wx = WXBizMsgCrypt(token, aeskey, corpid)
    timestamp = request.GET['timestamp']
    msg_signature = request.GET['msg_signature']
    nonce = request.GET['nonce']
    echostr = request.GET['echostr']
    ret, return_token = wx.VerifyURL(msg_signature, timestamp, nonce, echostr)
    if ret != 0:
       logger.info('............Error: Verify failed!!!')
    logger.info('timestamp:%s,msg_signature:%s,nonce:%s,echostr:%s', timestamp, msg_signature, nonce, echostr)
    logger.info(request.get_full_path())
    if request.GET.has_key('echostr'):
        logger.info(request.GET['echostr'])
        return HttpResponse(return_token)
    else:
        return HttpResponse('validate page')

def accesstoken(request):
    new_token = AccessToken.objects.get(pk=1)
    token = new_token.get_access_token()
    logger.info(token)
    return HttpResponse(token)
