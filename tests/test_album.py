from filmflow.models import Album
import pytest
from unittest import TestCase
from factories import AlbumFactory
from django.core.exceptions import ValidationError
from filmflow.views import show_albuns, album_detail, home

################################################ MODEL TESTS

def test_create_album(db):
	album = AlbumFactory()

	album.save()

def test_album_genre_too_big(db):
	album = AlbumFactory()
	album.genre = "genero muito grande, não deveria ter mais de 50 caracteres."

	with pytest.raises(ValidationError):
		album.full_clean()

def test_album_year_too_big(db):
	album = AlbumFactory()
	album.year = 2020

	with pytest.raises(ValidationError):
		album.full_clean()

def test_album_name_too_big(db):
	album = AlbumFactory()
	album.name = "nome do album muito grande, não deve ter mais de 100 caracteres e no momento se encontra maior que tal."
	
	with pytest.raises(ValidationError):
		album.full_clean()

def test_album_arthist_too_big(db):
	album = AlbumFactory()
	album.arthist = "nome do artista é muito grande, não deveria ter mais de 50 caracteres."

	with pytest.raises(ValidationError):
		album.full_clean()

def test_to_string(db):
	album = AlbumFactory()

	assert str(album) == album.name + "  [" + album.arthist + " - " + str(album.year) + "]"


################################################ VIEW TESTS

def test_albuns(rf, db):
    request = rf.get('/albuns/')
    response = show_albuns(request)
    assert response.status_code == 200

def test_album_detail(rf, db):
	album = AlbumFactory()
	album.save()

	request = rf.get('/album/' + str(album.id) + '/')
	response = album_detail(request, album.id)
	assert response.status_code == 200

#Testing Home
def test_home(rf):
	request = rf.get('/')
	response = home(request)
	assert response.status_code == 200