from django.conf.urls import include, url
from . import views

urlpatterns = [
    
    #login/
    url(r'^$', views.create_user, name = 'create_user'),

]