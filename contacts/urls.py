from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^intro/', include("home.urls")),
    # url(r'^tutorials/', include("tutorial.urls")),
    # url(r'^detector/', include("detector.urls")),
]