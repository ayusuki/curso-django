#coding: utf-8
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, TemplateView

from .views import teste_blog

urlpatterns = patterns('',
    url(r'^$', 'teste_blog', name='blog'),
    
)

