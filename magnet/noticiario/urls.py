from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import HomeView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    
)

