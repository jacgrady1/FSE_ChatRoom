from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app_chatroom.views.home', name='home'),
    url(r'^chat/(?P<username>\d+)$', 'app_chatroom.views.chat',name='chat'),
    url(r'^loggedin/', 'app_chatroom.views.userloggedin',name='userloggedin'),
    url(r'^refresh/', 'app_chatroom.views.refresh',name='refresh'),
    url(r'^admin/', include(admin.site.urls)),
)
