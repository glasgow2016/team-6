from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from brake_classroom.models import UserProject, Project
from datetime import datetime, timedelta
from django.http import JsonResponse


def index(request):
    return render(request, 'brake_classroom/index.html')


def walking(request):
    return render(request, 'brake_classroom/walking.html')


# def quiz(request):
#     level = request.GET['level']
#     question_number = int(request.GET['question'])
#     question = Question.objects.get(number=question_number, level=level)
#     count = Question.objects.filter(level=level).count()
#
#     previous_question = None if question_number == 1 else question_number - 1
#     next_question = None if question_number == count else question_number + 1
#     return render(request, 'brake_classroom/quiz.html',
#                   {'question': question, 'previous': previous_question, 'next': next_question})


def cycling(request):
    return render(request, 'brake_classroom/cycling.html')


def project(request):
    if request.method == 'GET':
        context = {}
        user_project = UserProject.objects.get(user=request.user)
        context['user_project'] = user_project
        return render(request, 'brake_classroom/project.html', context)
    else:
            mileage = request.POST['mileage']
            final_date = request.POST['final_date']
            days_to_complete = (datetime.strptime(final_date, "%Y-%m-%d") - datetime.now() + timedelta(days=1)).days
            new_project = Project(milage=mileage, complete_in=days_to_complete)
            new_project.save()
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


def update_performance(request):
    if request.is_ajax():
        new_distance = float(request.GET['new_distance'])
        new_money = float(request.GET['newMoney'])
        new_co2 = float(request.GET['newCO2'])
        project_id = int(request.GET['project_id'])

        the_project = Project.objects.get(id=project_id)
        the_project.goal_achieved += new_distance
        the_project.money_saved += new_money
        the_project.co2_saved += new_co2
        print("new money saved is %f" % the_project.money_saved)
        print("new co2 saved is %f" % the_project.co2_saved)
        the_project.save()

        return JsonResponse({'response': 'success'})
