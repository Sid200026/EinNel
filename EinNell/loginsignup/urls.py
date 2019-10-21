from django.urls import path
from . import views

app_name = 'loginsignup'

urlpatterns = [
    path('',views.index, name = "index"),
    path('login/',views.loginEmp, name = "login"),
    path('signup/', views.signupEmp, name = "signup"),
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('logout/', views.logoutEmp, name = "logout"),
    path('update/', views.update, name="update"),
    path('tasks/', views.task, name="task"),
    path('complete/',views.completetask, name="completetask"),
    path('alltasks/', views.alltasks, name="alltasks"),
    path('promote/', views.promote, name="promote"),
    path('contact/', views.contact, name = "contact"),
    path('review/', views.review, name="review"),
    path('rate/', views.rate, name="rate"),
    path('chat/', views.chat, name="chat"),
]
