from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    def __str__(self):
        return self.sname
class Course(models.Model):
    student=models.ManyToManyField(Student)
    cno=models.IntegerField()
    cname=models.CharField(max_length=100)
    cfee=models.IntegerField()
    def __str__(self):
        return self.cname


