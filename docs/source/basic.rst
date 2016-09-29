.. basic

============
基本接入指南
============

验证成为微信开发者
------------------------

在微信公众号后台填写相应的信息,如图所示,

.. image:: http://ww1.sinaimg.cn/mw690/a036a21agw1f2st9l46wsj216c11mjwp.jpg

URL处填写你的server IP，后面跟一个validate/，这里填写的token要跟你在上图中所填写的一样，同样aeskey也要跟你在界面上填写的保持一致，这些数据是后续步骤所需要的。 友情提示：如果你在验证过一次后对你的token或者EncodingAESKey做了修改.
把你微信公众平台的AppID,AppSecret,Token,AESKey,分别填写到settings.py文件中,运行`python manage.py shell`,新建一个AccessToken对象即可.