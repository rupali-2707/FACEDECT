from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView


app_name="teacher"
urlpatterns = [
    
path('',home_view),
path('teacherclick', teacherclick_view,name="teacherclick"),
path('teacherlogin', LoginView.as_view(template_name='teacherlogin.html'),name='teacherlogin'),
path('teachersignup', teacher_signup_view,name='teachersignup'),
path('teacher-dashboard', teacher_dashboard_view,name='teacher-dashboard'),
 path('afterlogin',afterlogin_view,name='afterlogin'),
]
