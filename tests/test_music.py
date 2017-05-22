from filmflow.models import Music
import pytest
from unittest import TestCase
from factories import MusicFactory
from django.core.exceptions import ValidationError


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


