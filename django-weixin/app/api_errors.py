'''
Created on Feb 3, 2015

@author: Rui, Gong

'''
from django.http import *
import json

import logging
logger = logging.getLogger("api")

def Http200(request, msg=u"Success",data=""):
    error = {
             u"code": u"200",
             u"message": msg,
             u"data": data
    }
    result = json.dumps(error)
#     logmsg = "user:%s failed with error:%s "%(request.user, msg)
#     logger.info(logmsg)
    return HttpResponse(result, content_type="application/json")

def Http400(request, msg=u"Bad Request",data=""):
    error = {
             u"code": u"400",
             u"message": msg,
             u"data": data
    }
    result = json.dumps(error)
    return HttpResponseBadRequest(result, content_type="application/json")

def Http401(request, msg=u"Unauthorized",data=""):
    error = {
             u"code": u"401",
             u"message": msg,
             u"data": data
    }
    result = json.dumps(error)
    return HttpResponseBadRequest(result, content_type="application/json")

def Http403(request, msg=u"Forbidden",data=""):
    error = {
             u"code": u"403",
             u"message": msg,
             u"data": data
    }
    result = json.dumps(error)
    return HttpResponseForbidden(result, content_type="application/json")

def Http404(request, msg=u"File not found",data=""):
    error = {
             u"code": u"404",
             u"message": msg,
             u"data": data
    }
    result = json.dumps(error)
    return HttpResponseNotFound(result, content_type="application/json")

def Http500(request, msg=u"Internal Server Error",data=""):
    error = {
             u"code": u"500",
             u"message": msg,
             u"data": data
    }
    result = json.dumps(error)
    return HttpResponseServerError(result, content_type="application/json")

