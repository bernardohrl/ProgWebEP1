from filmflow.models import Album
import pytest

# # from factories import AlbumFactory


# # def test_album_factory(album_factory):
# #     """Factories become fixtures automatically."""
# #     assert isinstance(album_factory, AlbumFactory)

# # def test_album(album):
# #     """Instances become fixtures automatically."""
# #     assert isinstance(album, Album)

# # @pytest.mark.parametrize("album__title", ["Mulher do Fim do Mundo"])
# # def test_parametrized(album):
# #     """You can set any factory attribute as a fixture using naming convention."""
# #     assert album.name == "Mulher do Fim do Mundo"


# from django.test import TestCase
# import factories

# class FilmflowAppCategoryTest(TestCase):

#     def test_if_category_is_displayed(self):
#         category = factories.AlbumFactory.create()

#         response = self.client.get('/')
#         self.assertTrue(album.name in response.content)




def test_create_album(db):
	album = Album(
		arthist = "artista",
		name = "nome",
		genre = "genero",
		year = 2000,
	)

	album.save()

def test_album_genre_too_big(db):
	album = Album(
		arthist = "bernardo",
		name = "nome",
		genre = "genero.muito.grande.nao.deveria.ter.mais.de.50.caracteres.e.ja.passou.dissos",
		year = 2000,
	)
	album.full_clean()
	album.save()