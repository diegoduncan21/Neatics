from django.conf.urls import patterns, include, url

urlpatterns = patterns('portal.views',
    
    url(r'^footer/$', 'footer', name='footer'),

    url(r'^barra_lateral/$', 'barra_lateral', name='barra_lateral'),
    url(r'^modal_logueo/$', 'modal_logueo', name='modal_logueo'),    
    url(r'^home/$', 'home', name='home'), 
    
    url(r'^template/(?P<template_name>\w+)/$', 'template', name='template'),
)
