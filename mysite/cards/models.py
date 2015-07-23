from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):

	qwner = models.ForeignKey(User)
	url = models.URLField()
	name = models.CharField(max_length=60)
	image = models.ImageField()
	media_type = models.CharField(max_length=32)
	created_at = models.DateTimeField('date published')


	def __str__(self):
		return self.name



