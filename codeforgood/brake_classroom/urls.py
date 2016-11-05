from django.conf.urls import url
from brake_classroom import views

urlpatterns = [
        url('^$', views.index, name='index'),
        url('^walking/', views.walking, name='walking'),
        url('^cycling/', views.cycling, name='cycling'),
        #url('^car-safety/', views.car_safety, name='car_safety'),
        url('^project/', views.project, name='project')
        ]

