from django.contrib import admin

# Register your models here.

from django.contrib import admin
from brake_classroom.models import Question, Project

admin.site.register(Question)
admin.site.register(Project)
