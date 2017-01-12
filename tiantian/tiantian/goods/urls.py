from django.conf.urls import url
import views

urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^$',views.index,name='index'),
<<<<<<< HEAD
    # url(r'^list/(\d+)/$',views.list,name='list'),
    # url(r'^detail/(\d+)/$',views.detail,name='detail'),
=======
    url(r'^list/(\d+)/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
>>>>>>> 44aabf271f60bb440ebadf54e6e9c8e1be169d46
    url(r'^list/(\d+)/(\d+)/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^immediatelyBuy/(\d+)/$',views.immediatelyBuy,name="addCart"),
    url(r'^addCart/$',views.addCart,name="add"),
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^userCenter/$',views.userCenter,name="userCenter"),
    url(r'^cart/$',views.cart,name="cart"),
    url(r'^order/$',views.order,name="order"),
    url(r'^logout/$',views.logout,name="logout"),
]
<<<<<<< HEAD
=======

>>>>>>> 44aabf271f60bb440ebadf54e6e9c8e1be169d46
