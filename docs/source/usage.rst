.. usage.rst

============
基本使用规则
============


获取AccessToken
-------------------

首先通过 `python manage.py shell` 新建一个AccessToken对象.

.. code-block:: python
   :linenos:

   from django_weixin.modesl import *
   a = AccessToken()
   a.save()

在代码中需要得到AccessToken的地方调用如下代码即可:

.. code-block:: python
   :linenos:

   from django_weixin.models import *
   a = AccessToken.objects.get(pk=1)
   access_token = a.get_access_token()

获取微信服务器列表
-------------------------

引用以下代码实现获取微信服务器列表,返回的是一个字符串列表.

.. code-block:: python
    :linenos:

    from django_weixin.models import *
    w = WeChatServer()
    server_ip_list = w.get_wechat_server_ip_list()
