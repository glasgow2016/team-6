from django.conf.urls import url
from brake_classroom import views

urlpatterns = [
        url('^$', views.index, name='index')
        ]

