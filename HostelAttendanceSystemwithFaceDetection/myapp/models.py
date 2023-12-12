from django.db import models

# Create your models here.
class Login(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    Post = models.CharField(max_length=100)
    Pin = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Parentname = models.CharField(max_length=100,default='0')
    Parentphonenumber = models.CharField(max_length=100,default='0')
    Department = models.CharField(max_length=100,default='0')
    AdmissionYear = models.CharField(max_length=100,default='0')
    Photo = models.CharField(max_length=500)
    # LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Attendance(models.Model):
    Date = models.DateField()
    Time = models.TimeField()
    SUDENT_ID = models.ForeignKey(Student,on_delete=models.CASCADE)
