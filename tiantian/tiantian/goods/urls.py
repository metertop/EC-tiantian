from django.conf.urls import url
import views

urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^$',views.index,name='index'),
    url(r'^list/$',views.list,name='list'),

]