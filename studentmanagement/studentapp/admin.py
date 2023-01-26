from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from studentapp.models import city, course, Student

admin.site.register(city)
admin.site.register(course)
admin.site.register(Student)
