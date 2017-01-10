from django.conf.urls import url
import views

urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^$',views.index,name='index'),
    url(r'^list/(\d+)/(\d+)/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^immediatelyBuy/(\d+)/$',views.immediatelyBuy,name="addCart"),
    url(r'^addCart/$',views.addCart,name="add"),
]