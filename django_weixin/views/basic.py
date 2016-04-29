# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import logging
from htmllib import HTMLParser
from django_weixin.api_errors import *
import json, xml.etree.ElementTree as et
from django_weixin.models.basic import *
from django_weixin.WXBizMsgCrypt import *
from django.views.decorators.csrf import csrf_exempt
from django_weixin.utils.utils import *
import xmlrpclib
from django.core import serializers


# Create your views here.

@csrf_exempt
def index(request):
    logging.info("#################enter ... ")
    if request.method == "GET":
        logging.info(request.method)
        # atoken = AccessToken.objects.get(id=1)
        corpid = settings.APP_ID
        aeskey = settings.AES_KEY
        token = settings.WX_TOKEN
        wx = WXBizMsgCrypt(token, aeskey, corpid)
        logging.info(request.GET)
        timestamp = request.GET['timestamp']
        msg_signature = request.GET['signature']
        nonce = request.GET['nonce']
        echostr = request.GET['echostr']
        ret, return_token = wx.VerifyURL(msg_signature, timestamp, nonce, echostr)
        logging.info(ret)
        logging.info(return_token)
        if ret != 0:
            logger.info('............Error: Verify failed!!!')
        logging.info('timestamp:%s,msg_signature:%s,nonce:%s,echostr:%s', timestamp, msg_signature, nonce, echostr)
        logging.info(request.get_full_path())
        if request.GET.has_key('echostr'):
            logging.info(request.GET['echostr'])
            return HttpResponse(return_token)
        else:
            return HttpResponse('validate page')

    elif request.method == "POST":
        # todo : judge if the message is valid
        # logging.info(request.REQUEST['signature'])
        logging.info(request.body)
        logging.info("\n\n")
        to_user_name = get_xml_text_by_property(request.body, "ToUserName")
        from_user_name = get_xml_text_by_property(request.body, "FromUserName")
        message_type = get_xml_text_by_property(request.body, "MsgType")
        create_time = get_xml_text_by_property(request.body, "CreateTime")
        origin_message_content = get_xml_text_by_property(request.body, "Content")
        message_content_list = [u"你个逗比", u"今天我要嫁给你", u"郭峻岭就是大肥", u"美好的一天开始了", u"让我们尽情骚动吧", u"让你回复,你还真特么回复啊!",
                                u"不要走,决战到天亮"]
        message_content = message_content_list[random.randint(0, len(message_content_list)) - 1]
        # logging.info(to_user_name)
        # logging.info(create_time)
        logging.info(message_type)
        if message_type == "event":  # 检测是不是event类型的消息
            event = get_xml_text_by_property(request.body, "Event")  # 获取event的类型
            if event == "scancode_waitmsg":  # 扫码但是不跳转的事件
                message_content = get_xml_text_by_property(request.body, "ScanResult")
            if event == "LOCATION":
                message_content = ""
        # root_element = et.Element('xml')
        # to_user_name_element = et.SubElement(root_element,'ToUserName')
        # to_user_name_element.text = '<![CDATA[' + to_user_name + ']]>'
        # from_user_name_element = et.SubElement(root_element,'FromUserName')
        # from_user_name_element.text = '<![CDATA[' + from_user_name + ']]>'
        # create_time_element = et.SubElement(root_element,'CreateTime')
        # create_time_element.text = create_time
        # message_type_element = et.SubElement(root_element,'MsgType')
        # message_type_element.text = '<![CDATA[' + message_type + ']]>'
        # content_element = et.SubElement(root_element,'Content')
        # content_element.text = '<![CDATA[' + "Hello" + ']]>'
        # xml_return_string = et.tostring(root_element)
        # logging.info(xml_return_string)

        # xml_return_string = TextMessage.TextMessageTemplate.format(toUser=from_user_name, fromUser=to_user_name,
        #                                                            create_time=create_time,
        #                                                            message_content=message_content)
        xml_return_string = KeFuMessage.KeFuMessageTemplate.format(toUser=from_user_name, fromUser=to_user_name,
                                                                   create_time=create_time,
                                                                   message_content=message_content)
        logging.info("\n\n")
        logging.info(xml_return_string)
        file_object = open("text_message.xml", 'w')
        file_object.write(xml_return_string)
        file_object.close()
        open_file = open('text_message.xml', 'r')
        file_string = open_file.read()
        open_file.close()

        return HttpResponse(file_string, content_type="text/xml")
    else:
        logging.info('...............other method.')
        return Http200(request)


def get_access_token_view(request):
    new_token = AccessToken.objects.get(pk=1)
    token = new_token.get_access_token()
    logging.info(token)
    context_data = {
        'access_token': token,
    }
    return render(request, 'get_access_token.html', context_data)


def admin_dashboard(request):
    access_token_url = settings.APP_URL + "/django-weixin/access/token/get/"
    qr_code_ticket = settings.APP_URL + "/django-weixin/show/ticket/"
    context_data = {
        "access_token_url": access_token_url,
        "qr_code_ticket": qr_code_ticket
    }
    return render(request, 'admin-dashboard.html', context_data)


def get_qr_code_ticket(request):
    from django_weixin.utils.utils import get_temp_qr_code,get_pergmanent_qr_code
    temp_url = get_temp_qr_code()
    pergmanent_url = get_pergmanent_qr_code()
    context_data = {
        'temp': temp_url,
        'permanent': pergmanent_url
    }
    return render(request, 'ticket.html', context_data)
