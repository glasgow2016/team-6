from django.shortcuts import render
from brake_classroom.models import Question, Level


def index(request):

    return render(request, 'brake_classroom/index.html')

def walking(request):

    return render(request, 'brake_classroom/walking.html')

def quiz(request):

    questions = Question.objects.order_by('number')
    if request.is_ajax():
        pass
        #answer = request.GET['answer']
    return render(request, 'brake_classroom/quiz.html', {'questions': questions})

def cycling(request):

    return render(request, 'brake_classroom/cycling.html')


def project(request):
    return render(request, 'brake_classroom/project.html')

