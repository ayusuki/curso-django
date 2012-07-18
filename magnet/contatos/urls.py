#coding: utf-8
from django.conf.urls import patterns, include, url

from .views import contato_simples

urlpatterns = patterns('',
    
    # Examples:
    url(r'^simples/$', contato_simples, name='contato-simples'),
   
)

