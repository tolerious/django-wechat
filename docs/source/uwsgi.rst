.. uwsgi

===========================
配置uwsgi
===========================

.. code-block:: python
   :linenos:

    [uwsgi]
    chdir = /home/tolerious/wechat_env/django-wechat # 项目目录
    env = DJANGO_SETTINGS_MODULE=wechat.settings
    module = wechat.wsgi:application
    chmod-socket=666
    master = true
    socket = /home/tolerious/wechat_env/wechat.sock # 随便你放在哪儿
    pidfile = /home/tolerious/wechat_env/wechat_uwsgi.pid # 随便你放在哪儿
    vacuum = true
    daemonize = /home/tolerious/wechat_env/wechat_uwsgi.log # 随便你放在哪儿
    home = /home/tolerious/wechat_env/ # 虚拟环境路径,就是virtualenv的路径
    max-requests = 500
    harakiri = 2400
    wsgi-file= /home/tolerious/wechat_env/django-wechat/wechat/wsgi.py # wsgi.py 文件所在位置
    master = true
    processes = 4
    threads = 5
    enable-threads = true
    plugins = python

配置uwsgi仅针对直接clone本项目进行开发的需求,如果使用 `pip` 进行安装的使用者可以忽略此部分配置