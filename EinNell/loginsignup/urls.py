from django.urls import path
from . import views

app_name = 'loginsignup'

urlpatterns = [
    path('',views.index, name = "index"),
    path('login/',views.login, name = "login"),
    path('signup/', views.signup, name = "signup"),
    path('dashboard/', views.dashboard, name = "dashboard"),
]
