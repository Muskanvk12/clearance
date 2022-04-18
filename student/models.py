from django.db import models
from django.contrib.auth.models import User
from teacher.models import Staffinfo

# Create your models here.
class Studentinfo(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	roll = models.IntegerField(blank=True, null=True, unique=True)
	year = models.IntegerField(blank=True, null=True, default=3)
	branch = models.CharField(default="CSE", max_length=100)
	sem = models.IntegerField(blank=True, null=True,default=6)
	status = models.IntegerField(blank=True, null=True)
	class Meta:
			ordering = ['id']

	# def __str__(self):
	# 	return self.student.username
