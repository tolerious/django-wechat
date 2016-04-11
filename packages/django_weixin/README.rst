=====
django-weixin
=====

Django-wechat采用Django框架实现微信公众号的开发.

详尽的文档在 "docs" 文件夹中.

Quick start
-----------

1. 添加'django-weixin'在你的setting.py文件中::

    INSTALLED_APPS = (
        ...
        'django_weixin',
    )

2. 配置URL路由::

    url(r'^django-weixin/', include('django_weixin.urls')),

3. 运行'python manage.py makemigrations && python manage.py migrate'命令来进行model的创建.
