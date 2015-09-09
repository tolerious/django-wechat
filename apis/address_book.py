'''
Created on 03 21, 2015

@author: tolerious

'''
from errors import *
from app.address_book import Department
import logging
def create_department(request):
    if request.method == "GET":
        logging.info("Called create_department API successfully")
        department = Department()
        department.name = "abec"
        department.create_department()
        department.save()
        return Http200(request)
    else:
        return Http200(request)