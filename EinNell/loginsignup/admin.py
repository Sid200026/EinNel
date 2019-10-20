from django.contrib import admin
from .models import Employee, Authority, Task
# Register your models here.

admin.site.register(Employee)
admin.site.register(Authority)
admin.site.register(Task)