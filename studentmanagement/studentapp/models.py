from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class city(models.Model):
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.city_name}"
class course(models.Model):
    course_name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.course_name}"
class Student(models.Model):
    student_name=models.CharField(max_length=50)
    student_age=models.IntegerField()
    student_Phnoe = models.BigIntegerField()
    student_city = models.ForeignKey(city,on_delete=models.CASCADE)
    student_course=models.ForeignKey(course,on_delete=models.CASCADE)
