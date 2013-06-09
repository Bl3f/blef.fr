from django.conf.urls import patterns, url
from front.views import *

urlpatterns = patterns('',
    url(r'^$', home),
)
