from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

app_name='student'
urlpatterns = [
path('studentclick', views.studentclick_view,name="studentclick"),
path('studentlogin', LoginView.as_view(template_name='studentlogin.html'),name='studentlogin'),
path('studentsignup', views.student_signup_view,name='studentsignup'),
path('student_dashboard', views.student_dashboard_view,name='student_dashboard'),
]