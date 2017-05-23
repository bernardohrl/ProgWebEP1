from django.conf.urls import url
from . import views

urlpatterns = [
    # film_flow/
    url(r'^$', views.home, name='film_flow_home'),

    # film_flow/albuns/
    url(r'^albuns/$', views.show_albuns, name='albuns_list'),

    # film_flow/musics/
    url(r'^musics/$', views.show_musics, name='musics_list'),

    # film_flow/albuns/:id
    url(r'^albuns/(?P<album_id>[0-9]+)/$', views.album_detail, name='album_detail'),

    # film_flow/music/:id
    url(r'^musics/(?P<music_id>[0-9]+)/$', views.music_detail, name='music_detail'),
]
