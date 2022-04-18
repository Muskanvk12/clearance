from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from .forms import LoginStaffForm
from django.contrib import messages
from .models import Designpattern
from .models import Artificialintelligence
from .models import Computernetwork
from .models import Sepm
from .models import Functionalenglish
from .models import Accountsection
from .models import Hod
from .models import Accountsection
from .models import Library
from .models import Scholarship
from .models import Sports
from .models import Ncc
from .models import Nss
from .models import Staffinfo
from student.models import Studentinfo
from .models import Final
# Create your views here.


def StaffLogin(request):
    '''for user authentication and login'''
    if request.user.is_authenticated:
        return HttpResponseRedirect('/staff/profile/')
    else:
        if request.method == 'POST':
            fm = LoginStaffForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                passwd = fm.cleaned_data['password']
                user = authenticate(username=uname, password=passwd)
                print(user)
                if user:
                    login(request, user)
                    return HttpResponseRedirect('/staff/profile/')
            else:
                messages.success(request, 'HEY')
                return render(request, 'teacher/login.html', {'form': fm})
        else:
            fm = LoginStaffForm()
            context = {
                'form': fm,
            }
            return render(request, 'teacher/login.html', context)


def StaffLogout(request):
    '''for user logout'''
    logout(request)
    return HttpResponseRedirect('/staff/')


def StaffProfile(request):
    if request.user.is_authenticated:
        # print(request.user.id)
        u = User.objects.get(pk=request.user.id)
        info = Staffinfo.objects.get(staff=u)
        print(info.subject)
        context = {
            'subject': info.subject
        }
        # u = User.objects.get(pk=request.user.id)
        # s = Staffinfo.objects.get(staff=u)
        # if s.id == 4:
        # 	d = Designpattern.objects.all()
        # 	context = {
        # 	'data': d,
        # 	}
        # return render(request, 'teacher/profile.html', context)
        # print(u)
        # print(dir(request.user.staffinfo.staff))
        # print(request.user.staffinfo.subject)
        return render(request, 'teacher/profile.html', context)
    return HttpResponseRedirect('/staff/')


def ViewRequest(request):
    if request.user.is_authenticated:
        # print(User.objects.get())
        u = User.objects.get(pk=request.user.id)
        s = Staffinfo.objects.get(staff=u)
        # print(s.id)
        if s.id == 9:
            d = Hod.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 10:
            d = Sepm.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 11:
            d = Functionalenglish.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 12:
            d = Designpattern.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 13:
            d = Artificialintelligence.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 14:
            d = Computernetwork.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 15:
            d = Accountsection.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 16:
            d = Library.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 17:
            d = Scholarship.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 18:
            d = Ncc.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 19:
            d = Nss.objects.all()
            context = {
                'data': d,
            }
        elif s.id == 20:
            d = Sports.objects.all()
            context = {
                'data': d,
            }
        return render(request, 'teacher/req.html', context)
        # return render(request, 'teacher/profile.html')
    return HttpResponseRedirect('/staff/')


def activate(request, userid):
    if request.user.is_authenticated:
        print(request.user.id)
        if request.method == 'POST':
            print(request.user.id)
            ut = User.objects.get(pk=request.user.id)
            st = Staffinfo.objects.get(staff=ut)
            us = User.objects.get(pk=userid)
            stu = Studentinfo.objects.get(student=us)
            sem = stu.sem
            year = stu.year
            roll = stu.roll
            name = stu.student.first_name + ' ' + stu.student.last_name
            if request.user.id == 8:
                a = Final.objects.get(stud=us)
                a.dp = "Clear"
                a.save()
                print(roll, name)
                d = Designpattern.objects.get(stud=us).delete()
            elif request.user.id == 4:
                f = Final.objects.create(
                    name=name, roll=roll, sem=sem, year=year, hod="Clear", stud=us)
                d = Hod.objects.get(stud=us).delete()
            elif request.user.id == 7:
                print("HEY 7")
                a = Final.objects.get(stud=us)
                a.fe = "Clear"
                a.save()
                print(roll, name)
                d = Functionalenglish.objects.get(stud=us).delete()
            elif request.user.id == 6:
                print("HEY 6")
                a = Final.objects.get(stud=us)
                a.sepm = "Clear"
                a.save()
                print(roll, name)
                d = Sepm.objects.get(stud=us).delete()
            elif request.user.id == 9:
                a = Final.objects.get(stud=us)
                a.ai = "Clear"
                a.save()
                print(roll, name)
                d = Artificialintelligence.objects.get(stud=us).delete()
            elif request.user.id == 10:
                print("HEY 10")
                a = Final.objects.get(stud=us)
                a.cn = "Clear"
                a.save()
                print(roll, name)
                d = Computernetwork.objects.get(stud=us).delete()
            elif request.user.id == 11:
                print("HEY")
                a = Final.objects.get(stud=us)
                a.acc = "Clear"
                a.save()
                d = Accountsection.objects.get(stud=us).delete()
            elif request.user.id == 12:
                a = Final.objects.get(stud=us)
                a.lib = "Clear"
                a.save()
                d = Library.objects.get(stud=us).delete()
                print("HEY 12")
            elif request.user.id == 22:
                a = Final.objects.get(stud=us)
                a.scholar = "Clear"
                a.save()
                d = Scholarship.objects.get(stud=us).delete()
                print("HEY 12")
            elif request.user.id == 23:
                a = Final.objects.get(stud=us)
                a.ncc = "Clear"
                a.save()
                d = Ncc.objects.get(stud=us).delete()
                print("HEY 12")
            elif request.user.id == 24:
                a = Final.objects.get(stud=us)
                a.nss = "Clear"
                a.save()
                d = Nss.objects.get(stud=us).delete()
                print("HEY 12")
            elif request.user.id == 25:
                a = Final.objects.get(stud=us)
                print("*" * 10)
                a.sports = "Clear"
                a.save()
                d = Sports.objects.get(stud=us).delete()
                print("HEY 12")
            return HttpResponseRedirect('/staff/profile')
    return HttpResponseRedirect('/staff/')


def reject(request, userid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            us = User.objects.get(pk=userid)
            if request.user.id == 8:
                a = Final.objects.get(stud=us)
                a.dp = "Denied"
                a.save()
                # print(roll, name)
                d = Designpattern.objects.get(stud=us).delete()
            elif request.user.id == 4:
                print(f"HELLO 'HOD'")
                # f = Final.objects.create(name=name, roll=roll, sem=sem, year=year,hod=1,stud=us)
                d = Hod.objects.get(stud=us).delete()
            elif request.user.id == 7:
                print("HEY 7")
                a = Final.objects.get(stud=us)
                a.fe = "Denied"
                a.save()
                # print(roll, name)
                d = Functionalenglish.objects.get(stud=us).delete()
            elif request.user.id == 6:
                print("HEY 6")
                a = Final.objects.get(stud=us)
                a.sepm = "Denied"
                a.save()
                # print(roll, name)
                d = Sepm.objects.get(stud=us).delete()
            elif request.user.id == 9:
                a = Final.objects.get(stud=us)
                a.ai = "Denied"
                a.save()
                # print(roll, name)
                d = Artificialintelligence.objects.get(stud=us).delete()
            elif request.user.id == 10:
                print("HEY 10")
                a = Final.objects.get(stud=us)
                a.cn = "Denied"
                a.save()
                # print(roll, name)
                d = Computernetwork.objects.get(stud=us).delete()
            elif request.user.id == 11:
                print("HEY")
                a = Final.objects.get(stud=us)
                a.acc = "Denied"
                a.save()
                d = Accountsection.objects.get(stud=us).delete()
            elif request.user.id == 12:
                a = Final.objects.get(stud=us)
                a.lib = "Denied"
                a.save()
                d = Library.objects.get(stud=us).delete()
                print("HEY 12")
            elif request.user.id == 22:
                a = Final.objects.get(stud=us)
                a.scholar = "Denied"
                a.save()
                d = Scholarship.objects.get(stud=us).delete()
                print("HEY 12")
            elif request.user.id == 23:
                a = Final.objects.get(stud=us)
                a.ncc = "Denied"
                a.save()
                d = Ncc.objects.get(stud=us).delete()
                print("HEY 12")
            elif request.user.id == 24:
                a = Final.objects.get(stud=us)
                a.nss = "Denied"
                a.save()
                d = Nss.objects.get(stud=us).delete()
                print("HEY 12")
            elif request.user.id == 25:
                a = Final.objects.get(stud=us)
                a.sports = "Denied"
                a.save()
                d = Sports.objects.get(stud=us).delete()
                print("HEY 12")
            return HttpResponseRedirect('/staff/profile')
    else:
        return HttpResponseRedirect('/staff/')
