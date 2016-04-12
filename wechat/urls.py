from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'wechat.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'django-weixin/', include('django_weixin.urls')),
                       # url(r'^validate/', include('django_weixin.urls', namespace='djangoweixin')),
                       url(r'^access/', include('django_weixin.urls')),
                       # url(r'api/', include('apis.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
