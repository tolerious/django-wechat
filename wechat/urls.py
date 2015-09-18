from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wechat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^validate/', include('app.urls', namespace='app')),
    url(r'^access/', include('app.urls')),
    # url(r'api/', include('apis.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
