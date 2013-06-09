from django.conf.urls import patterns, url
from front.views import *

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^home/$', home),
    url(r'^contact/$', contact),
)
