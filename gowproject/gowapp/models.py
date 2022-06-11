from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=30)    
    class Meta:
        db_table="Student"
class Studimg(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=30)
    gender_choices=[('M','Male'),('F','Female')]
    gender=models.CharField(choices=gender_choices,max_length=128)
    myimg=models.ImageField()    
    class Meta:
        db_table="Studimg"

# for auto validation purpose

class Empp(models.Model):
    firstname=models.CharField(max_length=15)
    email=models.EmailField()
    class Meta:
        db_table="Empp"

