from django.db import models
from django.contrib.auth.models import User


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
    co2_saved = models.FloatField( default=0)
    milage = models.FloatField()
    goal_achieved = models.FloatField(default=0)
    money_saved = models.FloatField(default=0)
    created = models.DateTimeField(null=True)
    complete_in = models.IntegerField(default=30)  # days


class UserProject(models.Model):
    user = models.OneToOneField(User)
    project = models.OneToOneField(Project, null=True)
