from django.contrib import admin
from .models import Employee, Authority, Task, Chat
# Register your models here.

admin.site.register(Employee)
admin.site.register(Authority)
admin.site.register(Task)
admin.site.register(Chat)