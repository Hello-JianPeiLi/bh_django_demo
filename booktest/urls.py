from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^create$', views.create),
    url(r'^remove/(\d+)$', views.remove),
    url(r'^detail/(\d+)$', views.detail),
    url(r'^area$', views.area),
    url(r'^login$', views.login),
    url(r'^check$', views.check),
    url(r'^login_ajax$', views.login_ajax),
]
