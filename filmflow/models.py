from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Album(models.Model):
	arthist = models.CharField(max_length = 50)
	name = models.CharField(max_length = 100)
	genre = models.CharField(max_length = 50)
	year = models.IntegerField(validators=[MaxValueValidator(2017), MinValueValidator(1900)])

	def __str__(self):
		return self.name + "  [" + self.arthist + " - " + str(self.year) + "]"


class Music(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name + " - " + self.album.arthist
