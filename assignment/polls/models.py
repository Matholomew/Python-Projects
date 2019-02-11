import datetime
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    incorrect_answers = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='General Knowledge')
    difficulty = models.CharField(max_length=200 ,default='Medium')


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    category = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=200)


class PlayerInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    highscore = models.CharField(max_length=200)
    tournaments_played = models.CharField(max_length=200)
