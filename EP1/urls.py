from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # take adm urls
    url(r'^admin/', include(admin.site.urls)),
    # take filmflow urls
    url(r'^film_flow/', include('filmflow.urls')),
    # take logins urls
    url(r'^login/', include('login.urls')),
]
