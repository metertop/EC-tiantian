from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$', views.cart, name='cart'),
    url(r'^remove_cart/', views.remove_cart, name='remove_cart'),
    url(r'^to_order/', views.to_order, name='to_order'),
]