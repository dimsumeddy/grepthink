from django.db import models

# Create your models here.

class Course(models.Model):
	course_name = models.CharField(max_length=30)

#class Project(models.Model):

#class User(models.Model):