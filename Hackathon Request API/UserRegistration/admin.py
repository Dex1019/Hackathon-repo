from django.contrib import admin
from .models import StudentRequest,CenterAllocated
# Register your models here.
admin.site.register(StudentRequest)
admin.site.register(CenterAllocated)