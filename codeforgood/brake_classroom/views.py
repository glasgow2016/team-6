from django.shortcuts import render


def index(request):

    return render(request, 'brake_classroom/index.html')

