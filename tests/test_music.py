from filmflow.models import Music
import pytest
from unittest import TestCase
from factories import MusicFactory
from django.core.exceptions import ValidationError
from filmflow.views import show_musics, music_detail


################################################ MODEL TESTS

def test_create_music(db):
	music = MusicFactory()
	music.save()


def test_music_name_too_big(db):
	music = MusicFactory()
	music.name = "nome da musica muito grande, não deve ter mais de 100 caracteres e no momento se encontra maior que tal."
	
	with pytest.raises(ValidationError):
		music.full_clean()

def test_to_string(db):
	music = MusicFactory()

	assert str(music) == music.name + " - " + music.album.arthist


################################################ VIEW TESTS

def test_musics(rf, db):
    request = rf.get('/music/')
    response = show_musics(request)
    assert response.status_code == 200

def test_music_detail(rf, db):
	music = MusicFactory()
	music.save()

	request = rf.get('/music/' + str(music.id) + '/')
	response = music_detail(request, music.id)
	assert response.status_code == 200


################################################ URL TESTS

@pytest.mark.urls('filmflow.urls')
def test_musics_url(client, db):
	assert client.get('/musics/').status_code == 200


@pytest.mark.urls('filmflow.urls')
def test_music_detail_url(client, db):
	music = MusicFactory()
	music.save()
	id  = music.id

	assert client.get('/musics/' + str(id) + '/').status_code == 200