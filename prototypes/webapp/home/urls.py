from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^intro/$', views.intro),
    url(r'^intro/overview', views.overview),
    url(r'^intro/history', views.history),
    url(r'^intro/numbers', views.numbers),
    url(r'^intro/location', views.location),
    url(r'^intro/status', views.status),


    url(r'^detector/', include("detector.urls")),
    url(r'^tutorials/', include("tutorial.urls")),
    url(r'^contacts/', include("contacts.urls")),
]