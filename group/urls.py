# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

# from logger.views import delete_instance


app_name = 'group'

urlpatterns = [

    url(r'^groups/$', views.group_list, name='groups_list'),
    url(r'^group_detail/(?P<group_id>[0-9]+)$', views.group_detail, name='group_detail'),
    url(r'^add_group/$', views.edit_group, name='add_group'),
    url(r'^edit_group/(?P<group_id>[0-9]+)$', views.edit_group, name='edit_group'),
    url(r'^deletion/$', views.remove_group, name='deletion'),
    url(r'^remove_group/(?P<group_id>[0-9]+)/', views.remove_group, kwargs={'instance_type': 2}, name='remove_group'),

]
