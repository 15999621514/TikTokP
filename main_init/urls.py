#-*- coding: utf-8 -*-
#开发人员: Wolf
#开发团队: ELSTP Studio
#联系方式: QQ:1465217851 emal:15999621514@163.com
#开发时间: 2019/12/25 18:34
#开发IDE : 
#文件名  : urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from main_init.views import index, api_url
urlpatterns = [
    url(r'^$', index),
    url(r'^get_url$', api_url)
    #path('admin/', admin.site.urls),
]
