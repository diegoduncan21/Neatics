from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'^login/$', 'custom_login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^register/$', 'register', name='register'),
    
    url(r'^index/$', 'index', name='index'),
    
)
