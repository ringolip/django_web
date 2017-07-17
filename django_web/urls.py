
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('ringolip.urls', namespace='ringolip')),

    url(r'^users/', include('users.urls', namespace='users')),
]
