# -*- coding: utf-8 -*-

from django.conf.urls import url
from students import views

app_name = 'students'

urlpatterns = [

    url(r'^students/$', views.student_list, name='students_list'),
    url(r'^add_student/$', views.edit_student, name='add_student'),
    url(r'^edit_student/(?P<student_id>[0-9]+)$', views.edit_student, name='edit_student'),
    url(r'^deletion/$', views.remove_student, name='deletion'),
    url(r'^remove_student/(?P<student_id>[0-9]+)/', views.remove_student, kwargs={'instance_type': 1}, name='remove_student'),

]
