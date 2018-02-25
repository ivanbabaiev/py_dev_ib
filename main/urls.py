# -*- coding: utf-8 -*-

from django.conf.urls import url
from main.views import logout
from . import views
from group.views import group_list

app_name = 'main'

urlpatterns = [

    url(r'^$', group_list, name='index'),
    url(r'^logout/$', logout, name='logout'),

]
