﻿from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^', include('information.urls')),
    url(r'grappelli', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("teacher.urls")),
    url(r'^', include('information.urls'))
)

if settings.DEBUG:
	urlpatterns += patterns('',
 	   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
