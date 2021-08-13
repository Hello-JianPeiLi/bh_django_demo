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
    url(r'^index2$', views.index2),
    url(r'^index_login$', views.index_login),
    url(r'^template_login_check$', views.template_login_check),
    url(r'^upload_file$', views.upload_file),
    url(r'^handle_file$', views.handle_file),
    url(r'^upload_ajax_file$', views.upload_ajax_file),
    # 获取图片路径下发到web
    url(r'^get_pic$', views.get_pic),
    # 获取省级地区
    url(r'^get_prov$', views.get_prov),
    # 获取city
    url(r'^city/(\d+)$', views.city),
    # 获取dis
    url(r'^dis/(\d+)$', views.dis),
]
