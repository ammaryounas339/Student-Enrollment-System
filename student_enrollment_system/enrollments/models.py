from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()


class Course(models.Model):
    title = models.CharField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

