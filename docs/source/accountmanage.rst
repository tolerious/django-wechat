.. accountmanage

==================================
账号管理
==================================


生成30天有效期的二维码
--------------------------------

在需要获得公众号二维码链接的地方调用如下代码.

.. code-block:: python

    from django_weixin.utils.utils import *
    temp_url = get_temp_qr_code()


生成永久有效的二维码
-----------------------------------

.. code-block:: python

    from django_weixin.utils.utils import *
    pergmanent_url = get_pergmanent_qr_code()