from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Authority(models.Model):
    authUser = models.OneToOneField(User, on_delete=models.CASCADE)
    numberOfUsers = models.IntegerField(blank = True, default = 0)

    def __str__(self):
        return self.authUser.username

class Employee(models.Model):
    empUser = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank = True, null = True)
    travel = models.IntegerField(blank = True, null = True)
    attrition = models.IntegerField(blank = True, null = True)
    dr = models.IntegerField(blank = True, null = True)
    department = models.IntegerField(blank = True, null = True)
    distance = models.IntegerField(blank = True, null = True)
    ed = models.IntegerField(blank = True, null = True)
    education = models.IntegerField(blank = True, null = True)
    envsatisfaction = models.IntegerField(blank = True, null = True)
    gender = models.IntegerField(blank = True, null = True) # Yes male,   No femaile
    hourlyRate = models.IntegerField(blank = True, null = True)
    involvment = models.IntegerField(blank = True, null = True)
    joblevel = models.IntegerField(blank = True, null = True)
    role = models.IntegerField(blank = True, null = True)
    satisfaction = models.IntegerField(blank = True, null = True)
    marital_status = models.IntegerField(blank = True, null = True)
    income = models.IntegerField(blank = True, null = True)
    monthly_rate = models.IntegerField(blank = True, null = True)
    prevCompanies = models.IntegerField(blank = True, null = True)
    overage = models.IntegerField(blank = True, null = True, default = 1)
    overtime = models.IntegerField(blank = True, null = True) #True means Yes False means No
    salaryHike = models.IntegerField(blank = True, null = True)
    rating = models.CharField(blank = True, null = True, max_length = 50)
    relsatisfaction = models.IntegerField(blank = True, null = True)
    # Standard hours is always 80
    stock = models.IntegerField(blank = True, null = True)
    workingYears = models.IntegerField(blank = True, null = True)
    lastTrainingTime = models.IntegerField(blank = True, null = True)
    workLifeBalance = models.IntegerField(blank = True, null = True)
    yearsAtCompany = models.IntegerField(blank = True, null = True)
    yearsInCurrentRole = models.IntegerField(blank = True, null = True)
    lastprom = models.IntegerField(blank = True, null = True)
    curManager = models.IntegerField(blank = True, null = True)
    senior = models.ForeignKey(Authority, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.empUser.username

class Task(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    auth = models.ForeignKey(Authority, on_delete=models.CASCADE, blank=True, null=True)
    task = models.CharField(max_length = 100, primary_key=True)
    lastDate = models.DateField()
    completedDate = models.DateField(blank = True, null = True)
    rating = models.DecimalField(blank = True, null = True, decimal_places=1, max_digits=2)

    def __str__(self):
        return self.task

class Chat(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    auth = models.ForeignKey(Authority, on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField(blank = True, null = True, max_length = 100)

    def __str__(self):
        return self.writer.username + self.auth.authUser.username