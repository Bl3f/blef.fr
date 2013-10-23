from django.conf.urls import patterns, url
from front.views import index, home, contact, resume, portfolio

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^home/$', home),
    url(r'^contact/$', contact),
    url(r'^resume/$', resume),
    url(r'^portfolio/$', portfolio),
)
