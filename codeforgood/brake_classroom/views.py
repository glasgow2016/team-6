from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from brake_classroom.models import Question


def index(request):
    return render(request, 'brake_classroom/index.html')


def walking(request):
    return render(request, 'brake_classroom/walking.html')
    #
    # def quiz(request):
    #     questions = Question.objects.all()


def quiz(request):
    print("Request")
    print(request.GET)
    level = request.GET['level']
    question_number = int(request.GET['question'])
    question = Question.objects.get(number=question_number, level=level)
    count = Question.objects.filter(level=level).count()

    previous_question = None if question_number == 1 else question_number - 1
    next_question = None if question_number == count else question_number + 1
    return render(request, 'brake_classroom/quiz.html',
                  {'question': question, 'previous': previous_question, 'next': next_question})


def cycling(request):
    return render(request, 'brake_classroom/cycling.html')


def project(request):
    return render(request, 'brake_classroom/project.html')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    login(request, user)
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')
