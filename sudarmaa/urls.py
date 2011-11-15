from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^", include('books.urls')),
    url(r"^", include('dictionary.urls')),
    # accounts
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
        'template_name': 'registration/login.html',
    }, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/'
    }, name='logout'),
    # admin
    url(r"^admin/", include(admin.site.urls)),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
    urlpatterns += patterns('',
        url(r'^site_media/media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
