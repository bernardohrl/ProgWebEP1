from filmflow.models import Album
from filmflow.models import Music
import factory

class AlbumFactory(factory.Factory):
	class Meta:
		model = Album

	id = 0
	arthist = 'Baina System'
	name = 'Duas Cidades'
	genre = 'Samba & Rock & Rap'
	year = 2015


class MusicFactory(factory.Factory):
	class Meta:
		model = Music

	album = factory.SubFactory(AlbumFactory)
	name = 'Duas Cidades'