from django.conf.urls import patterns, url
from swarm import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^submit-job/$', views.submit_job, name='submit-job'),
	url(r'^success/$', views.success, name='success'),
	url(r'^details/$', views.details, name='details'),
	url(r'^docs/$', views.documentation, name='docs')
)