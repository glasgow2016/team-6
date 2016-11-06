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
    questions = Question.objects.order_by('number')
    if request.is_ajax():
        pass
        # answer = request.GET['answer']
    return render(request, 'brake_classroom/quiz.html', {'questions': questions})


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
