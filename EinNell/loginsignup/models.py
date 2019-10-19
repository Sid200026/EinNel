from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank = True)
    travel = models.IntegerField(blank = True)
    attrition = models.BooleanField(blank = True)
    dr = models.IntegerField(blank = True)
    department = models.CharField(max_length = 50, blank = True)
    distance = models.IntegerField(blank = True)
    ed = models.IntegerField(blank = True)
    education = models.CharField(max_length = 50, blank = True)
    satisfaction = models.IntegerField(blank = True)
    gender = models.BooleanField(blank = True) # Yes male,   No femaile
    hourlyRate = models.IntegerField(blank = True)
    involvment = models.IntegerField(blank = True)
    joblevel = models.IntegerField(blank = True)
    role = models.CharField(max_length = 50,blank = True)
    satisfaction = models.IntegerField(blank = True)
    marital_status = models.IntegerField(blank = True)
    income = models.IntegerField(blank = True)
    monthly_rate = models.IntegerField(blank = True)
    prevCompanies = models.IntegerField(blank = True)
    # Over 18 field can be computed from age
    overtime = models.BooleanField(blank = True) #True means Yes False means No
    salaryHike = models.IntegerField(blank = True)
    rating = models.IntegerField(blank = True)
    relsatisfaction = models.IntegerField(blank = True)
    # Standard hours is always 80
    stock = models.IntegerField(blank = True)
    workingYears = models.IntegerField(blank = True)
    lastTrainingTime = models.IntegerField(blank = True)
    workLifeBalance = models.IntegerField(blank = True)
    yearsAtCompany = models.IntegerField(blank = True)
    yearsInCurrentRole = models.IntegerField(blank = True)
    lastprom = models.IntegerField(blank = True)
    curManager = models.IntegerField(blank = True)

    def __str__(self):
        return self.user.username
