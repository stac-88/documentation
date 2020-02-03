from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index),
   #  url(r'^/detector/magnets', views.overview),
   #  url(r'^intro/history', views.history),
   #  url(r'^intro/numbers', views.numbers),
   #  url(r'^intro/location', views.location),
   #  url(r'^intro/status', views.status),
   #
   # url(r'^/detector/', views.overview),
   # url(r'^/detector/magnets', views.overview),
   # url(r'^/detector/bbc', views.overview),
   # url(r'^/detector/dc">DC</a>
   # url(r'^/detector/pc">PC</a>
  # <a class="nav-link" href="/detector/rich">RICH</a>
  # <a class="nav-link" href="/detector/tof">TOF</a>
  # <a class="nav-link" href="/detector/emcal">EMCal</a>
  # <a class="nav-link" href="/detector/mutr">MuTr</a>
  # <a class="nav-link" href="/detector/muld">MulD</a>
  # <a class="nav-link" href="/detector/zdc">ZDC</a>
  # <a class="nav-link" href="/detector/tofw">TOF-W</a>
  # <a class="nav-link" href="/detector/focal">FoCal (internal)</a>
  # <a class="nav-link" href="/detector/mpc">MPC (internal)</a>
  # <a class="nav-link" href="/detector/fcal">FCAL</a>
  # <a class="nav-link" href="/detector/mvd">MVD</a>
  # <a class="nav-link" href="/detector/highpt">High-pT</a>
  # <a class="nav-link" href="/detector/vtx">VTX</a>
  # <a class="nav-link" href="/detector/fvtx">FVTX</a>
  # <a class="nav-link" href="/detector/hbd">HBD</a>
  # <a class="nav-link" href="/detector/frdupgrade">Forward Upgrade</a>

    # url(r'^intro/', include("home.urls")),
    # url(r'^tutorials/', include("tutorial.urls")),
    # url(r'^contacts/', include("contacts.urls")),
]