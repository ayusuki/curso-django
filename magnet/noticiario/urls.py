#coding: utf-8
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView

from .views import HomeView
from .models import Noticia 
urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^news/(?P<pk>\d+)$', DetailView.as_view(model=Noticia), name='noticia-detalhe'),    
)

