from django.conf.urls import url
from brake_classroom import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^walking/', views.walking, name='walking'),
    url('^cycling/', views.cycling, name='cycling'),
    url('^project/', views.project, name='project'),
    url('^login/$', views.login_user, name="login"),
    url('^logout/$', views.logout_user, name='logout'),
    url('^update_performance/$', views.update_performance, name='update_performance')
]
