from django.shortcuts import render


def index(request):

    return render(request, 'brake_classroom/index.html')

def walking(request):

    return render(request, 'brake_classroom/walking.html')

def quiz(request):
    questions = Question.objects.all()

    return render(request, 'brake_classroom/quiz.html', {'questions': questions})

def cycling(request):

    return render(request, 'brake_classroom/cycling.html')


def project(request):
    return render(request, 'brake_classroom/project.html')

