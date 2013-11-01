from django.conf.urls import patterns, url
from front.views import index, me, contact, resume, portfolio

urlpatterns = patterns('',
                       url(r'^$',
                           index,
                           name="index"),

                       url(r'^me/$',
                           me,
                           name="me"),

                       url(r'^contact/$',
                           contact,
                           name="contact"),

                       url(r'^resume/$',
                           resume,
                           name="resume"),

                       url(r'^portfolio/$',
                           portfolio,
                           name="portfolio"),
                       )
