from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)  # อนุญาตให้ว่างได้
    email = models.EmailField()
