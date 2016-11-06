from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from brake_classroom.models import Question, UserProject
from brake_classroom.forms import ProjectForm


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
    if request.method == 'GET':
        context = {}
        user_project = UserProject.objects.get(user=request.user)
        context['user_project'] = user_project
        context['project_form'] = ProjectForm()
        return render(request, 'brake_classroom/project.html', context)
    else:
        project_form = ProjectForm(request.POST)

        if project_form.is_valid():
            new_project = project_form.save()
            user_project = UserProject.objects.get(user_id=request.POST['user_id'])
            user_project.project = new_project
            user_project.save()
            return redirect('/project/')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    login(request, user)
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')
