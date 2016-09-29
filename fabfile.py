# -*- coding: utf-8 -*-
'''
Created on 04 07, 2016

@author: tolerious

'''

from fabric.api import *

env.roledefs = {
    't': ['tolerious@wx.meiparking.com']
}


def m(b="master", c=" "):
    with settings(warn_only=True):
        local("source ~/.zshrc&&source ../bin/activate && python manage.py collectstatic --noinput")
        local("git commit -am '  %s ;'&&git push origin %s" % (c, b))
        local("mkdir -p packages/django_weixin")
        local("cp -R django_weixin packages/django_weixin")
        # local("cd packages/django_weixin/dist/ && rm *")
        # local("cd packages/django_weixin && python setup.py sdist")
        # local("cd packages/django_weixin && twine upload dist/*")
    with cd("/home/tolerious/wechat_env/django-wechat"):
        run("git stash")
        commend = "git ck %s" % b
        run("git fetch")
        print commend
        run(commend)
        run("git pull origin %s" % b)
        run("source ../bin/activate")
        run("source ../bin/activate&&python manage.py collectstatic --noinput")
        run("cd .. && python restart_uwsgi.py uwsgi_wechat.ini")


def build():
    with settings(warn_only=True):
        local("source ../bin/activate && python manage.py collectstatic --noinput")
        local("mkdir -p packages/django_weixin")
        local("cp -R django_weixin packages/django_weixin")
        local("cd packages/django_weixin/dist/ && rm *")
        local("cd packages/django_weixin && python setup.py sdist")
        local("cd packages/django_weixin && twine upload dist/*")


def p(b, c=" 我们一起啪啪啪 "):
    with settings(warn_only=True):
        local("git commit -am ' update..., %s ;'&&git push origin %s" % (c, b))
    with cd("/home/tolerious/wechat_env/django-wechat"):
        run("git stash")
        commend = "git ck %s" % b
        run("git fetch")
        print commend
        run(commend)
        run("git pull origin %s" % b)
        run("source ../bin/activate")
        run("source ../bin/activate&&python manage.py collectstatic")
        # run("cd .. && python restart_uwsgi.py uwsgi.ini")
