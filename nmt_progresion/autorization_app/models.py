from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 35)
    surname = models.CharField(max_length = 35)
    fatherly = models.CharField(max_length = 35, blank = True, default = False)
    grade = models.CharField(max_length = 5, blank = True, default = False)
    occupation = models.CharField(max_length = 35)
    password = models.CharField(max_length = 35, default = False)
    date_of_birth = models.DateField()