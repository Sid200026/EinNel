from django.urls import path
from . import views

app_name = 'loginsignup'

urlpatterns = [
    path('',views.index, name = "index"),
    path('login/',views.loginEmp, name = "login"),
    path('signup/', views.signupEmp, name = "signup"),
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('logout/', views.logoutEmp, name = "logout"),
    path('update', views.update, name="update"),
    path('tasks', views.task, name="task"),
    path('complete',views.completetask, name="completetask"),
]
