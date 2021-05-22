
"""
    Author         : Jagat Iyer
    Developer     : Prasanna Vijayan
    Created Date : 10th Jan 2015
    Description     : All the urls for user navigation is configured here
    Projct Name     : PostReplyPrasanna
    Last Updated : 14 Jan 2015
                                    """

from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'postreply.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^', include('registration.backends.default.urls')),
    url(r'^home/$', 'postandreply.views.postform', name="homepage"),
    url(r'^add/$', 'postandreply.views.addpost', name="addpost"),    
    url(r'^reply/$', 'postandreply.views.addreply', name="addreply"),    
    url(r'^like/$', 'postandreply.views.addlikes', name="addlike"),
    url(r'^replylike/$', 'postandreply.views.replylikes', name="replylike"),    
    url(r'^getdata/$', 'postandreply.views.getdata', name="getdata"),    
)

if settings.DEBUG:
    
    urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.MEDIA_ROOT}),
                    )
