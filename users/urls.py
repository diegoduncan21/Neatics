from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^singup/$', 'singup', name='singup'),
    
    url(r'^index/$', 'index', name='index'),
    
)
