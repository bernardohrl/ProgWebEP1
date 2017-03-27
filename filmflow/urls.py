from django.conf.urls import include, url
from . import views

urlpatterns = [
    
    #film_flow/
    url(r'^$', views.home),

    #film_flow/albuns/
    url(r'^albuns/$', views.show_albuns),

    # #film_flow/musics/
    # url(r'^/musics/$', views.show_musics),

]