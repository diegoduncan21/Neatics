from django.conf.urls import patterns, include, url

urlpatterns = patterns('portal.views',
    
    url(r'^footer/$', 'footer', name='footer'),
    url(r'^barra_lateral/$', 'barra_lateral', name='barra_lateral'), 
    url(r'^home/$', 'home', name='home'),    
)