from django.conf.urls import url
from policy_tracker_app import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^restricted/$', views.restricted, name='restricted'),
	url(r'^profile/settings/$', views.profile_settings, name='profile_settings'),
    url(r'^profile/settings/password/$', views.profile_password, name='profile_password'),
	url(r'^contactus/$', views.contactus, name='contactus'),
]
