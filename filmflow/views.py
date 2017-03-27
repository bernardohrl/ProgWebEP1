from django.shortcuts import render
from .models import Album, Music

def home(request):
    return render(request, 'filmflow/home.html', {})


    								#Album
def show_albuns(request):
	albuns = Album.objects.all()
	return render(request, 'filmflow/albuns.html', {'albuns' : albuns})

def album_detail(request, album_id):
	album = Album.objects.get(id=album_id)
	return render(request, 'filmflow/album_detail.html', {'album' : album})



									#Music
def show_musics(request):
	musics = Music.objects.all()
	return render(request, 'filmflow/musics.html', {'musics' : musics})
