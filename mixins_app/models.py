from django.db import models

# Create your models here.
class Student(models.Model):
    studentname=models.CharField(primary_key=True,max_length=50, default=False)
    def __str__(self):
        return self.studentname

class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    teacher_name=models.CharField(max_length=50)
    def __str__(self):
        return self.teacher_name
class Atendence(models.Model):
    status_CHOICES = (
        ('Present', 'Presentt'),
        ('Absent', 'Absent'),
    )
    statues = models.CharField(max_length=1, choices=status_CHOICES, default=False)
    teachename=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    studentname=models.ForeignKey(Student,on_delete=models.CASCADE)





