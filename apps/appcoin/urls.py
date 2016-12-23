from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new', views.newpage),
    url(r'^currency/create$', views.createCurrency),
    url(r'^appcoin/create$', views.createAppCoin),
    url(r'^showCurrency/(?P<id>\d+)$', views.showCurrency),
    url(r'^showAppCoin/(?P<id>\d+)$', views.showAppCoin),
]
