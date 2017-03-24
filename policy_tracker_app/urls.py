from django.conf.urls import url
from policy_tracker_app import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^countries/add_country/$', views.add_country, name='add_country'),
	url(r'^countries/(?P<country_name_slug>[\w\-]+)/$', views.country, name='country'),
	url(r'^countries/(?P<country_name_slug>[\w\-]+)/add_policy/$', views.add_policy, name='add_policy'),
	url(r'^policy/(?P<policy_id>[\w\-]+)/$', views.policy, name='policy'),
	url(r'^register/$', views.register, name='register'),
	url(r'^countries/$', views.countries, name='countries'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^profile/settings/$', views.profile_settings, name='profile_settings'),
    url(r'^profile/settings/password/$', views.profile_password, name='profile_password'),
	url(r'^contactus/$', views.contactus, name='contactus'),
	url(r'^faq/$', views.faq, name='faq'),
	url(r'^news/$', views.news, name='news'),
]
