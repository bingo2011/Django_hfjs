from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'hfjs.views.index'),
    url(r'(?P<template>.+\.html)$', 'django.views.generic.simple.direct_to_template'), 
)

