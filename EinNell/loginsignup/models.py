from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    empUser = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank = True, null = True)
    travel = models.IntegerField(blank = True, null = True)
    attrition = models.BooleanField(blank = True, null = True)
    dr = models.IntegerField(blank = True, null = True)
    department = models.CharField(max_length = 50, blank = True, null = True)
    distance = models.IntegerField(blank = True, null = True)
    ed = models.IntegerField(blank = True, null = True)
    education = models.CharField(max_length = 50, blank = True, null = True)
    satisfaction = models.IntegerField(blank = True, null = True)
    gender = models.BooleanField(blank = True, null = True) # Yes male,   No femaile
    hourlyRate = models.IntegerField(blank = True, null = True)
    involvment = models.IntegerField(blank = True, null = True)
    joblevel = models.IntegerField(blank = True, null = True)
    role = models.CharField(max_length = 50,blank = True, null = True)
    satisfaction = models.IntegerField(blank = True, null = True)
    marital_status = models.IntegerField(blank = True, null = True)
    income = models.IntegerField(blank = True, null = True)
    monthly_rate = models.IntegerField(blank = True, null = True)
    prevCompanies = models.IntegerField(blank = True, null = True)
    # Over 18 field can be computed from age
    overtime = models.BooleanField(blank = True, null = True) #True means Yes False means No
    salaryHike = models.IntegerField(blank = True, null = True)
    rating = models.IntegerField(blank = True, null = True)
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

    def __str__(self):
        return self.user.username
