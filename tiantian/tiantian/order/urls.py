# coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
	url(r'^placeOrder/$', views.placeOrder),
	url(r'^userCenterOrder/$', views.userCenterOrder),
	url(r'^pageTab/$',views.pageTab)
]