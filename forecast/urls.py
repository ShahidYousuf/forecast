from django.conf.urls import url
from . import views
app_name = 'forecast'
urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^update/$', views.update, name='update'),
   url(r'^detail/(?P<div>[0-5]{1})/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<time>\d+:\d+:\d+)/$', views.detail, name='detail'),
]