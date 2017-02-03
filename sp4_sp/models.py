from django.db import models

# Create your models here.
class Student(models.Model):
    学号     = models.CharField(max_length=100)
    姓名     = models.CharField(max_length=100)
    身份证号 = models.CharField(max_length=100)
    def __str__(self):
        return self.姓名

class MIS(models.Model):
    姓名 = models.CharField(max_length=100)
    学号 = models.CharField(max_length=100)
    身份证号 = models.CharField(max_length=100)
    def __str__(self):
        return self.姓名

class Admin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name