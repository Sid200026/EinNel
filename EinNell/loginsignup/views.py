from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Employee, Authority, Task, Chat
from django.contrib.auth.models import User 
from django.utils import timezone
from django.core.mail import EmailMessage
from .predictionModel import predictModel

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
        user = request.user
        auth = Authority.objects.get(authUser = user)
        emp = Employee.objects.filter(senior = auth)
        return render(request, 'loginsignup/dashboard_auth.html', {'auth':auth, 'emp':emp})
    elif request.user.is_active :
        user = request.user
        emp = Employee.objects.get(empUser = user)
        tasks = Task.objects.filter(emp = emp, completedDate = None)
        count = tasks.count()
        return render(request, 'loginsignup/dashboard_emp.html', {'emp':emp, 'len':count})
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def update(request):
    if request.method == 'POST':
        try:
            user = request.user
            emp = Employee.objects.get(empUser = user)
            emp.age = int(request.POST.get('age'))
            emp.travel = int(request.POST.get('travel'))
            emp.attrition = int(request.POST.get('attrition'))
            emp.dr = int(request.POST.get('dr'))
            emp.department = int(request.POST.get('department'))
            emp.distance = int(request.POST.get('distance'))
            emp.ed = int(request.POST.get('ed'))
            emp.education = int(request.POST.get('education'))
            emp.envsatisfaction = int(request.POST.get('esatisfaction'))
            emp.gender = int(request.POST.get('gender'))
            emp.hourlyRate = int(request.POST.get('hourlyrate'))
            emp.involvment = int(request.POST.get('involvment'))
            emp.joblevel = int(request.POST.get('joblevel'))
            emp.role = int(request.POST.get('role'))
            emp.satisfaction = int(request.POST.get('satisfaction'))
            emp.marital_status = int(request.POST.get('maritalstatus'))
            emp.income = int(request.POST.get('income'))
            emp.monthly_rate = int(request.POST.get('monthlyrate'))
            emp.prevCompanies = int(request.POST.get('prevCompanies'))
            if int(request.POST.get('age'))>18:
                emp.overage = 1
            else:
                emp.overage = 0
            emp.overtime = int(request.POST.get('overtime'))
            emp.salaryHike = int(request.POST.get('salary'))
            emp.relsatisfaction = int(request.POST.get('rsatisfaction'))
            emp.stock = int(request.POST.get('stock'))
            emp.workingYears = int(request.POST.get('working'))
            emp.lastTrainingTime = int(request.POST.get('lastTrainingTime'))
            emp.workLifeBalance = int(request.POST.get('worklife'))
            emp.yearsAtCompany = int(request.POST.get('yearsAtComp'))
            emp.yearsInCurrentRole = int(request.POST.get('yearsAtCur'))
            emp.lastprom = int(request.POST.get('lastprom'))
            emp.curManager = int(request.POST.get('curManager'))
            emp.save()
            return HttpResponseRedirect(reverse('loginsignup:dashboard'))
        except:
            user = request.user
            emp = Employee.objects.get(empUser = user)
            if emp.age != None:
                return render(request, 'loginsignup/askhr.html')
            return render(request, 'loginsignup/updateEmployee.html', {'error':'Only Numeric Values are allowed'})
    if request.user.is_staff:
        return render(request, 'loginsignup/dashboard_auth.html')
    elif request.user.is_active :
        user = request.user
        emp = Employee.objects.get(empUser = user)
        if emp.age != None:
            return render(request, 'loginsignup/askhr.html')
        return render(request, 'loginsignup/updateEmployee.html')
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def task(request):
    if request.method == 'POST':
        if request.user.is_staff:
            try:
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
            except:
                user = request.user
                auth = Authority.objects.get(authUser = user)
                emps = Employee.objects.filter(senior = auth)
                return render(request, 'loginsignup/task_auth.html', {'emp':emps, 'error':"No such Employee Exists"})
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
            try:
                taskname = request.POST.get('tasks')
                task = Task.objects.get(task = taskname)
                task.completedDate = timezone.now()
                task.save()
                user = request.user
                emp = Employee.objects.get(empUser = user)
                getTask = Task.objects.filter(emp = emp, completedDate=None)
                return render(request, 'loginsignup/complete.html', {'tasks':getTask})
            except:
                user = request.user
                emp = Employee.objects.get(empUser = user)
                getTask = Task.objects.filter(emp = emp, completedDate=None)
                return render(request, 'loginsignup/complete.html', {'tasks':getTask, 'error':'No such task exists'})
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
        tasks = Task.objects.filter(auth = auth)[::-1]
        return render(request, 'loginsignup/viewalltasks.html' ,{'tasks':tasks})
    elif request.user.is_active :
        return render(request, 'loginsignup/dashboard_emp.html')
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def promote(request):
    if request.method == 'POST':
        if request.user.is_staff:
            try:
                user = request.user
                auth = Authority.objects.get(authUser = user)
                emps = request.POST.get('emp')
                empsuser = User.objects.get(username = emps)
                emp = Employee.objects.get(empUser=empsuser )
                empsuser.is_staff = True
                empsuser.save()
                Authority.objects.create(authUser=empsuser)
                emp.delete()
                return HttpResponseRedirect(reverse('loginsignup:dashboard'))
            except:
                user = request.user
                auth = Authority.objects.get(authUser = user)
                emp = Employee.objects.filter(senior = auth)
                return render(request, 'loginsignup/promote.html', {'emp':emp, 'error':'No such employee exists'})
    if request.user.is_staff:
        user = request.user
        auth = Authority.objects.get(authUser = user)
        emp = Employee.objects.filter(senior = auth)
        return render(request, 'loginsignup/promote.html', {'emp':emp})
    elif request.user.is_active :
        return render(request, 'loginsignup/dashboard_emp.html')
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def contact(request):
    if request.method == 'POST':
        if request.user.is_staff:
            try:
                name = request.user.username
                textbody = request.POST.get('email')
                empname = request.POST.get('id')
                user = User.objects.get(username = empname)
                employee = Employee.objects.get(empUser = user)
                email = EmailMessage('Mail from {}'.format(name), textbody, to=[user.email])
                email.send()
                return HttpResponseRedirect(reverse('loginsignup:dashboard'))
            except:
                user = request.user
                auth = Authority.objects.get(authUser = user)
                emp = Employee.objects.filter(senior = auth)
                return render(request, 'loginsignup/sendmailauth.html', {'emp':emp, 'error':'No such Employee Exists'})

        else:
            name = request.user.username
            textbody = request.POST.get('email')
            emp = Employee.objects.get(empUser = request.user)
            email = EmailMessage('Mail from {}'.format(name), textbody, to=[emp.senior.authUser.email])
            email.send()
            return HttpResponseRedirect(reverse('loginsignup:dashboard'))
    if request.user.is_staff:
        user = request.user
        auth = Authority.objects.get(authUser = user)
        emp = Employee.objects.filter(senior = auth)
        return render(request, 'loginsignup/sendmailauth.html', {'emp':emp})
    elif request.user.is_active :
        return render(request, 'loginsignup/sendmailemp.html')
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def review(request):
    if request.method == 'POST' and request.user.is_staff:
        try:
            user = request.user
            auth = Authority.objects.get(authUser = user)
            empuser = request.POST.get('emp')
            usr = User.objects.get(username = empuser)
            emp = Employee.objects.get(empUser = usr)
            employee = Employee.objects.filter(senior = auth)
            arr = [emp.age,emp.attrition,emp.travel,emp.dr,emp.department,emp.distance,emp.ed,emp.education,
                    1,emp.envsatisfaction,emp.gender,emp.hourlyRate,emp.involvment,emp.joblevel,emp.role,
                    emp.satisfaction, emp.marital_status,emp.income,emp.monthly_rate,emp.prevCompanies,
                    emp.overage,emp.overtime,emp.salaryHike,emp.relsatisfaction,80,emp.stock,emp.workingYears,
                    emp.lastTrainingTime,emp.workLifeBalance,emp.yearsAtCompany,emp.yearsInCurrentRole,
                    emp.lastprom,emp.curManager
            ]
            res = predictModel(arr)
            res['accuracy'] = round(res['accuracy']*100,2)
            if(res['result'] == [5]):
                res['result'] = "Excellent"
            elif(res['result'] == [4]):
                res['result'] = "Very Good"
            elif(res['result'] == [3]):
                res['result'] = "Good"
            elif(res['result'] == [2]):
                res['result'] = "Poor"
            elif(res.result == [1]):
                res['result'] = "Worst"
            emp.rating = res['result']
            emp.save()
            return render(request, 'loginsignup/review.html' , {'emp':employee, 'result':res, 'name':empuser})
        except:
            user = request.user
            auth = Authority.objects.get(authUser = user)
            employee = Employee.objects.filter(senior = auth)
            return render(request, 'loginsignup/review.html' , {'emp':employee, 'err':'The selected employee has not updated his profile yet or does not exist'})
    if request.user.is_staff:
        user = request.user
        auth = Authority.objects.get(authUser = user)
        emp = Employee.objects.filter(senior = auth)
        return render(request, 'loginsignup/review.html' , {'emp':emp})
    elif request.user.is_active:
        return render(request, 'loginsignup/dashboard_emp.html')
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def rate(request):
    if request.method == 'POST' and request.user.is_staff:
        try:
            user = request.user
            auth = Authority.objects.get(authUser = user)
            tasktext = request.POST.get('task')
            task = Task.objects.get(task = tasktext)
            rating = request.POST.get('rating')
            task.rating = rating
            task.save()
            tasks = Task.objects.filter(auth = auth, completedDate = None, rating = None)
            star = {1,2,3,4,5}
            return render(request, 'loginsignup/rate.html' , {'tasks':tasks, 'star':star})
        except:
            user = request.user
            auth = Authority.objects.get(authUser = user)
            tasks = Task.objects.filter(auth = auth, rating = None).exclude(completedDate=None)
            star = {1,2,3,4,5}
            return render(request, 'loginsignup/rate.html' , {'tasks':tasks, 'star':star,'error':'No such task exists'})
    if request.user.is_staff:
        user = request.user
        auth = Authority.objects.get(authUser = user)
        tasks = Task.objects.filter(auth = auth, rating = None).exclude(completedDate=None)
        star = {1,2,3,4,5}
        return render(request, 'loginsignup/rate.html' , {'tasks':tasks, 'star':star})
    elif request.user.is_active:
        return render(request, 'loginsignup/dashboard_emp.html')
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))

def chat(request):
    if request.method == 'POST':
        if request.user.is_staff:
            user = request.user
            auth = Authority.objects.get(authUser = user)
            content = request.POST.get('content')
            Chat.objects.create(writer = user, auth = auth, content = content)
            chat = Chat.objects.filter(auth = auth)[::-1]
            return render(request, 'loginsignup/chatauth.html',{'chat':chat, 'usr':user.username})
        if request.user.is_active:
            user = request.user
            emp = Employee.objects.get(empUser = user)
            auth = emp.senior       
            content = request.POST.get('content')
            Chat.objects.create(writer = user, auth = auth, content = content)    
            chat = Chat.objects.filter(auth = auth)[::-1]
            return render(request, 'loginsignup/chatemp.html',{'chat':chat, 'usr':user.username})
    if request.user.is_staff:
        user = request.user
        auth = Authority.objects.get(authUser = user)
        chat = Chat.objects.filter(auth = auth)[::-1]
        return render(request, 'loginsignup/chatauth.html',{'chat':chat, 'usr':user.username})
    elif request.user.is_active :
        user = request.user
        emp = Employee.objects.get(empUser = user)
        auth = emp.senior
        chat = Chat.objects.filter(auth = auth)[::-1]
        return render(request, 'loginsignup/chatemp.html',{'chat':chat, 'usr':user.username})
    else:
        return HttpResponseRedirect(reverse('loginsignup:login'))