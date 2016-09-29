# -*- coding: utf-8 -*-
'''
Created on 04 11, 2016

@author: tolerious

'''


import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-weixin',
    version='0.1.6',
    packages=['django_weixin'],
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple Django application to implementation Wechat API.',
    long_description=README,
    url='http://tobe.engineer/',
    author='tolerious',
    author_email='tolerious@qq.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)