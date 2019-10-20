from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Employee, Authority, Task
from django.contrib.auth.models import User 
from django.utils import timezone

def assignEmployeeToAuthority():
    auth = Authority.objects.all().order_by('numberOfUsers')
    senior = auth[0]
    senior.numberOfUsers += 1
    senior.save()
    return senior


def index(request):
    return render(request, 'loginsignup/index.html')

def loginEmp(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('loginsignup:dashboard'))
        else:
            return render(request, 'loginsignup/login.html', {'error':'Wrong Username and Password Combination'})
    return render(request, 'loginsignup/login.html')

def signupEmp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            user = User.objects.create_user(username = username, email = email, password = password)
        except:
            return render(request, 'loginsignup/signup.html', {'error':'The username or email already exists'})
        if user:
            login(request, user)
            senior = assignEmployeeToAuthority()
            emp = Employee.objects.create(empUser = user, senior=senior)
            return HttpResponseRedirect(reverse('loginsignup:dashboard'))
        else:
            return render(request, 'loginsignup/signup.html', {'error':'The username or email already exists'})
    return render(request, 'loginsignup/signup.html')

def logoutEmp(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginsignup:login'))

def dashboard(request):
    if request.user.is_staff:
        return render(request, 'loginsignup/dashboard_auth.html')
    elif request.user.is_active :
        return render(request, 'loginsignup/dashboard_emp.html')
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def update(request):
    if request.user.is_staff:
        return render(request, 'loginsignup/dashboard_auth.html')
    elif request.user.is_active :
        user = request.user
        emp = Employee.objects.get(empUser = user)
        return render(request, 'loginsignup/updateEmployee.html', {'user':emp})
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def task(request):
    if request.method == 'POST':
        if request.user.is_staff:
            auth = Authority.objects.get(authUser = request.user)
            task = request.POST.get('taskname')
            lastdate = request.POST.get('lastdate')
            emp = request.POST.get('employee')
            user = User.objects.get(username = emp)
            employee = Employee.objects.get(empUser = user)
            try:
                Task.objects.create(emp = employee, auth = auth, task = task,lastDate = lastdate)
                return HttpResponseRedirect(reverse('loginsignup:dashboard'))
            except:
                user = request.user
                auth = Authority.objects.get(authUser = user)
                emps = Employee.objects.filter(senior = auth)
                return render(request, 'loginsignup/task_auth.html', {'emp':emps, 'error':"This task has already been created"})
        if request.user.is_active:
            return HttpResponseRedirect(reverse('loginsignup:completetask'))
    if request.user.is_staff:
        user = request.user
        auth = Authority.objects.get(authUser = user)
        emps = Employee.objects.filter(senior = auth)
        return render(request, 'loginsignup/task_auth.html', {'emp':emps})
    elif request.user.is_active :
        user = request.user
        emp = Employee.objects.get(empUser = user)
        getTask = Task.objects.filter(emp = emp, completedDate=None)
        return render(request, 'loginsignup/task_emp.html', {'tasks':getTask})
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def completetask(request):
    if request.method == 'POST':
        if request.user.is_active:
            taskname = request.POST.get('tasks')
            task = Task.objects.get(task = taskname)
            task.completedDate = timezone.now()
            task.save()
            user = request.user
            emp = Employee.objects.get(empUser = user)
            getTask = Task.objects.filter(emp = emp, completedDate=None)
            return render(request, 'loginsignup/complete.html', {'tasks':getTask})
    if request.user.is_staff:
        return render(request, 'loginsignup/dashboard_auth.html')
    elif request.user.is_active :
        user = request.user
        emp = Employee.objects.get(empUser = user)
        getTask = Task.objects.filter(emp = emp, completedDate=None)
        return render(request, 'loginsignup/complete.html', {'tasks':getTask})
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def alltasks(request):
    if request.user.is_staff:
        user = request.user
        auth = Authority.objects.get(authUser = user)
        tasks = Task.objects.filter(auth = auth)
        return render(request, 'loginsignup/viewalltasks.html' ,{'tasks':tasks})
    elif request.user.is_active :
        return render(request, 'loginsignup/dashboard_emp.html')
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))