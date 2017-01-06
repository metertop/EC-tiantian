from django.conf.urls import url
import views

urlpatterns=[
    # url(r'^index/$', index, name='index'),
    # url(r'^$', index, name='index'),
    # url(r'^login/$',login, name='login'),
    # url(r'^loginHandle/$', loginHandle),
    # url(r'^register/$',register,name="register"),
    # url(r'^registerHandle/$',registerHandle),
	url(r'^index/$',views.index, name='index'),
	url(r'^$',views.index, name='index'),
	url(r'^login/$',views.login, name='login'),
	url(r'^loginHandle/$', views.loginHandle),
	url(r'^register/$',views.register,name="register"),
	url(r'^registerHandle/$',views.registerHandle),
	url(r'^checkReName/$',views.checkReName),
	url(r'^checkUname/$',views.checkUname),
	url(r'^user_center_info/$',views.user_center_info),
	url(r'^user_center_site/$',views.user_center_site),
	url(r'^recInfoHandle/$',views.recInfoHandle),
]