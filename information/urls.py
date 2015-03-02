from django.conf.urls import patterns, url
from information import views

urlpatterns = patterns('',
	url('^$',views.speciality_list, name = "speciality_list"),
	url(r'^subject/create/$', views.create_subject, name='create_subject'),
	url(r'^labs/create/(\d+)/$', views.create_lab, name='create_lab'),
	url(r'^labs/list/(\d+)/$', views.teacher_labs_list, name='teacher_labs_list'),
	url(r'^theory/create/(\d+)$', views.create_theory, name='create_theory'),
	url(r'^subject/delete/(\d+)/$', views.delete_subject, name='delete_subject'),
	url(r'^subject/edit/(\d+)/$', views.edit_subject, name='edit_subject'),
	url(r'^teacher/admin/$', views.teacher_subject_list, name='teacher_subject_list'),
	url(r'^(?P<speciality_id>\d+)/$', views.course_list, name='course_list'),
	url(r'^(?P<speciality_id>\d+)/(?P<course_id>\d+)/$', views.subject_list, name='subject_list'),
)