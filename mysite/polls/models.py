import datetime


from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __repr__(self):
		return '< {} - {} >'.format(self.pk, self.question_text)

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'





class Choice(models.Model):
	question = models.ForeignKey(Question, related_name='choice')
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

