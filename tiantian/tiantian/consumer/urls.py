from django.conf.urls import url
import views

urlpatterns=[
	url(r'^login/$',views.login, name='login'),
	url(r'^loginout/$',views.loginout),
	url(r'^loginHandle/$', views.loginHandle),
	url(r'^register/$',views.register,name="register"),
	url(r'^registerHandle/$',views.registerHandle),
	url(r'^checkReName/$',views.checkReName),
	url(r'^checkReEmail/$',views.checkReEmail),
	url(r'^checkUname/$',views.checkUname),
	url(r'^user_center_info/$',views.user_center_info),
	url(r'^user_center_site/$',views.user_center_site),
	url(r'^recInfoHandle/$',views.recInfoHandle),
]