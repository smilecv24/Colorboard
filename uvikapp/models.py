from django.db import models


class Game(models.Model):
	players = models.IntegerField()
	squares = models.IntegerField()
	cards = models.IntegerField()
	sequence = models.CharField(max_length=100)
	cardList = models.CharField(max_length=1000)
	result = models.CharField(max_length=100)
