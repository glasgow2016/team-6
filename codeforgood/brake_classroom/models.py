from django.db import models


# Create your models here.
class Level(models.Model):
    level = models.IntegerField()

    def __unicode__(self):
        return self.level


class Question(models.Model):
    number = models.IntegerField()
    question_title = models.TextField(max_length=500)
    right_answer = models.CharField(max_length=128)
    wrong_answer1 = models.CharField(max_length=128)
    wrong_answer2 = models.CharField(max_length=128)
    wrong_answer3 = models.CharField(max_length=128)
    popup = models.TextField(max_length=500)
    level = models.ForeignKey(Level)

    def __unicode__(self):
        return self.question_title


class Project(models.Model):
    co2_saved = models.FloatField()
    milage = models.FloatField()
    money_saved = models.FloatField()
