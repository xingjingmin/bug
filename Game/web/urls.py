#！、usr/bin/env python
#-*- coding:utf-8 -*-

from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    re_path('^(?P<student_id>[0-9]+)/modfy$', views.Modfy, name='modfy'),
    path('add/', views.Add, name='add'),
    path('add/', views.Add, name='add'),
    re_path('^(?P<student_id>[0-9]+)/dele$', views.Dele, name='dele'),
]
