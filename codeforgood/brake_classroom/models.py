from django.db import models


class Question(models.Model):
    level = models.CharField(max_length=20)
    number = models.IntegerField()
    question_title = models.TextField(max_length=500)
    right_answer = models.CharField(max_length=128)
    wrong_answer1 = models.CharField(max_length=128)
    wrong_answer2 = models.CharField(max_length=128)
    wrong_answer3 = models.CharField(max_length=128)

    def __unicode__(self):
        return self.question_title


class Project(models.Model):
    co2_saved = models.FloatField()
    milage = models.FloatField()
    money_saved = models.FloatField()
