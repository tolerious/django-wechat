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


.. code-block:: python
   :linenos:

   from django_weixin.models import *
   a = AccessToken.objects.get(pk=1)
   access_token = a.get_access_token()