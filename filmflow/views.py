from django.shortcuts import render
from .models import Album, Music

def home(request):
    return render(request, 'filmflow/home.html', {})


def show_albuns(request):
	albuns = Album.objects.all()
	return render(request, 'filmflow/albuns.html', {'albuns' : albuns})
