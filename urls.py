from django.conf.urls import patterns, include, url

urlpatterns = patterns('hfjs.views',
    url(r'^$', 'index'),
    url(r'donuts_result/$', 'donuts_result'),
    url(r'bannerocity_result/$', 'bannerocity_result'),
)

urlpatterns += patterns('',
    url(r'(?P<template>.+\.html)$', 'django.views.generic.simple.direct_to_template'), 
)
