from django.db import models

class Question(models.Model):
	qestion_text = models.CharField('question text', max_length = 200)
	pub_date = models.DateTimeField('publication date')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField('choice text', max_length = 200)
	votes = models.IntegerField(default = 0)