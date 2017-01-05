from django.conf.urls import url
import views

urlpatterns=[
	url(r'^index/$', index, name='index'),
    url(r'^$', index, name='index'),
    url(r'^login/$',login, name='login'),
    url(r'^loginHandle/$', loginHandle),
    url(r'^register/$',register,name="register"),
    url(r'^registerHandle/$',registerHandle),
]