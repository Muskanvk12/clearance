from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Staffinfo(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    dept = models.CharField(max_length=100, default="CSE")

    class Meta:
        ordering = ['id']
    # def _str_(self):
    # 	return self.staff.username


class Designpattern(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Artificialintelligence(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Computernetwork(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Functionalenglish(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Sepm(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Hod(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Library(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Accountsection(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Sports(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Ncc(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Nss(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Scholarship(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100)
    sem = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Final(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    roll = models.IntegerField(null=True, blank=True)
    sem = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    hod = models.CharField(max_length=100, null=True, blank=True)
    sepm = models.CharField(max_length=100, null=True, blank=True)
    fe = models.CharField(max_length=100, null=True, blank=True)
    dp = models.CharField(max_length=100, null=True, blank=True)
    ai = models.CharField(max_length=100, null=True, blank=True)
    cn = models.CharField(max_length=100, null=True, blank=True)
    acc = models.CharField(max_length=100, null=True, blank=True)
    lib = models.CharField(max_length=100, null=True, blank=True)
    scholar = models.CharField(max_length=100, null=True, blank=True)
    sports = models.CharField(max_length=100, null=True, blank=True)
    ncc = models.CharField(max_length=100, null=True, blank=True)
    nss = models.CharField(max_length=100, null=True, blank=True)
