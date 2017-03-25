from django.db import models

class Album(models.Model):
	arthist = models.CharField(max_length = 200)
	name = models.CharField(max_length = 300)
	genre = models.CharField(max_length = 50)
	year = models.IntegerField()

	def __str__(self):
		return self.name + "  [" + self.arthist + " - " + str(self.year) + "]"


class Music(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name + " - " + self.album.arthist
