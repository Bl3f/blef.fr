from django.conf.urls import patterns, url
from front.views import index, me, contact, resume, _portfolio, workip

urlpatterns = patterns('',
                       url(r'^portfolio/$',
                           _portfolio,
                           name="portfolio"),

                       url(r'^.*$',
                           workip,
                           name="workip"),

                       #url(r'^me/$',
                       #    me,
                       #    name="me"),

                       #url(r'^contact/$',
                       #    contact,
                       #    name="contact"),

                       #url(r'^resume/$',
                       #    resume,
                       #    name="resume"),
                       )
