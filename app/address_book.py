'''
Created on 03 19, 2015

@author: tolerious

'''
from django.db import models
from models import *
import requests,json,logging,pprint

class Department(models.Model):
    name = models.CharField(max_length="100",default="")
    parentid = models.IntegerField(default=1)
    order = models.IntegerField(default=1)
    department_id = models.IntegerField(default=-1)

    def __unicode__(self):
        return self.name + ";" + str(self.department_id)

    def create_department(self):
        dic = {
            "name":self.name,
            "parentid":self.parentid,
        }
        accesstoken = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=" + accesstoken
        data = json.dumps(dic)
        r = requests.post(url,data=data)
        return_dic = r.json()
        logging.info(return_dic)
        ids = return_dic["id"]
        self.department_id = ids
        return ids

    def update_department(self):
        dic = {
            "id": self.department_id,
            "name": self.name,
        }
        accesstoken = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=" + accesstoken
        data = json.dumps(dic)
        r = requests.post(url,data=data)
        return_dic = r.json()
        logging.info(return_dic)
        return return_dic

    def delete_department(self):
        accesstoken = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=" + accesstoken + "&id=" + str(self.department_id)
        r = requests.get(url)
        return_dic = r.json()
        logging.info(return_dic)

    def get_department_list(self):
        accesstoken = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=" + accesstoken + "&id=" + str(self.department_id)
        r = requests.get(url)
        return_dic = r.json()
        logging.info(return_dic)
        return return_dic

class Employee(models.Model):
    userid = models.CharField(default="",max_length=100,blank=False)
    name = models.CharField(default="",blank=False,max_length=100)
    department_list = models.TextField(default="[1]", blank=False)
    position = models.CharField(default="", max_length=100)
    mobile = models.CharField(default="",max_length=100)
    email = models.CharField(default="",max_length=100)
    weixinid = models.CharField(default="",max_length=100)
    extattr = models.TextField(default='{"attrs":[]}', blank=False)

    def __unicode__(self):
        return self.userid + ";" + self.weixinid

    def create_member(self):
        access_token = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=" + access_token
        dump_department_list = json.loads(self.department_list)
        print self.extattr
        exta_dic = json.loads(self.extattr)
        dic = {
            "userid": self.userid,
            "name": self.name,
            "department":dump_department_list,
            "position":self.position,
            "mobile":self.mobile,
            "email":self.email,
            "weixinid":self.weixinid,
            "extattr":exta_dic,
        }
        data = json.dumps(dic)
        r = requests.post(url,data=data)
        return_json = r.json()
        logging.info(return_json)
        self.save()
        return return_json

    def update_member(self):
        access_token = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=" + access_token
        dump_department_list = json.loads(self.department_list)
        print self.extattr
        exta_dic = json.loads(self.extattr)
        dic = {
            "userid": self.userid,
            "name": self.name,
            "department":dump_department_list,
            "position":self.position,
            "mobile":self.mobile,
            "email":self.email,
            "weixinid":self.weixinid,
            "extattr":exta_dic,
        }
        data = json.dumps(dic)
        r = requests.post(url,data=data)
        return_json = r.json()
        logging.info(return_json)
        return return_json

    def delete_member(self):
        access_token = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=" + access_token + "&userid=" + str(self.userid)
        r = requests.get(url)
        return_json = r.json()
        logging.info(return_json)
        return return_json

    def delete_bulk_members(self,delete_list):
        access_token = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?access_token=" + access_token
        dic = {
            "useridlist": delete_list
        }
        data = json.dumps(dic)
        r = requests.post(url,data=data)
        return_json = r.json()
        logging.info(return_json)
        return return_json

    def get_employee_info(self):
        access_token = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=" + access_token + "&userid=" + self.userid

        r = requests.get(url)
        return_json = r.json()
        logging.info(return_json)
        return return_json

    # may need to improve
    def get_department_employee_info(self,department_id,fetch_child="1",status="0"):
        access_token = AccessToken.objects.get(id=1).get_access_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token="+ access_token +"&department_id=" + str(department_id) + "&fetch_child="+ fetch_child+ "&status=" + status
        r = requests.get(url)
        return_json = r.json()
        logging.info(return_json)
        return return_json

    def get_department_employee_deatil_info(self,department_id,fetch_child="1",status="0"):
        pass