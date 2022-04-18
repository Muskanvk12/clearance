from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .forms import AddUserForm, LoginUserForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from teacher.models import Staffinfo
from .forms import UpdateProfileForm
from .models import Studentinfo
from teacher.models import Designpattern
from teacher.models import Artificialintelligence
from teacher.models import Computernetwork
from teacher.models import Sepm
from teacher.models import Functionalenglish
from teacher.models import Accountsection
from teacher.models import Hod
from teacher.models import Accountsection
from teacher.models import Library
from teacher.models import Final
from teacher.models import Sports
from teacher.models import Ncc
from teacher.models import Nss
from teacher.models import Scholarship
# Create your views here.


def HomePage(request):
    return render(request, 'student/index.html')


def UserSignUp(request):
    '''to create user'''
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    else:
        if request.method == 'POST':
            fm = AddUserForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Account Created !!!')
                fm = AddUserForm()
                context = {
                    'form': fm,
                }
                return render(request, 'student/signup.html', context)
            else:
                return render(request, 'student/signup.html', {'form': fm})
        else:
            fm = AddUserForm()
            context = {
                'form': fm,
            }
            return render(request, 'student/signup.html', context)


def UserLogin(request):
    '''for user authentication and login'''
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    else:
        if request.method == 'POST':
            fm = LoginUserForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                passwd = fm.cleaned_data['password']
                user = authenticate(username=uname, password=passwd)
                print(user)
                if user:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
                else:
                    # pass
                    print('hey')
            else:
                return render(request, 'student/login.html', {'form': fm})
        else:
            fm = LoginUserForm()
            context = {
                'form': fm,
            }
            return render(request, 'student/login.html', context)


def UserLogout(request):
    '''for user logout'''
    logout(request)
    return HttpResponseRedirect('/')


def UserProfile(request):
    # print(dir(request))
    # print(request.get_raw_uri())
    if request.user.is_authenticated:
        # print(dir(request.user.studentinfo))
        # print(request.user.studentinfo.year)
        return render(request, 'student/profile.html')
    return HttpResponseRedirect('/')


def sublist(request):
    # print(request.user.id)
    if request.user.is_authenticated:
        u = User.objects.get(pk=request.user.id)
        try:
            f = Final.objects.get(stud=u)
            l = [f.hod, f.sepm, f.fe, f.dp, f.ai, f.cn, f.acc,
                 f.lib, f.scholar, f.ncc, f.nss, f.sports]
        except Exception as E:
            a = Staffinfo.objects.all()
            context = {
                'data': a,
            }
            return render(request, 'student/sublist.html', context)
    # if f.hod==1:
    # 	print("HEY")
        a = Staffinfo.objects.all()
        context = {
            'data': a,
            'l': l,
        }
        return render(request, 'student/sublist.html', context)
    return HttpResponseRedirect('/')


def getClearance(request, userid):
    if request.method == 'POST':
        u = User.objects.get(pk=userid)
        s = Studentinfo.objects.get(student=u)
        name = s.student.first_name + ' '+s.student.last_name
        sem = s.sem
        roll = s.roll
        year = s.year
        dept = s.branch
        postId = request.POST['staffid']
        if postId == '9':
            c = Hod.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '10':
            c = Sepm.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '11':
            c = Functionalenglish.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '12':
            c = Designpattern.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '13':
            c = Artificialintelligence.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '14':
            c = Computernetwork.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '15':
            c = Accountsection.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '16':
            c = Library.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '17':
            c = Scholarship.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '18':
            c = Ncc.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '19':
            c = Nss.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        elif postId == '20':
            c = Sports.objects.create(
                name=name, sem=sem, roll=roll, year=year, dept=dept, stud=u)
            print(f"{postId} Created")
        return HttpResponseRedirect('/profile/list')
        # return render(request, 'student/sublist.html')
    return HttpResponseRedirect('/')


def UpdateProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            prof = UpdateProfileForm(request.POST)
            u = User.objects.get(pk=request.user.id)
            if prof.is_valid():
                roll = prof.cleaned_data['roll']
                year = prof.cleaned_data['year']
                sem = prof.cleaned_data['sem']
                branch = prof.cleaned_data['branch']
                print(roll, year, sem, branch)
                p = Studentinfo.objects.create(
                    roll=roll, year=year, sem=sem, branch=branch, student=u)
                # print(request.POST)
                # print('ID',u)
            # f.save()
            return HttpResponseRedirect('/profile')
        else:
            try:
                s = Studentinfo.objects.get(student=request.user)
            except Exception as E:
                a = UpdateProfileForm()
                f = Studentinfo(request.POST)
                context = {
                    'profile': a,
                    'update': 'Please Update'
                }
                return render(request, 'student/profileupdate.html', context)
                print(E)
            a = UpdateProfileForm()
            f = Studentinfo(request.POST)
            print(f)
            context = {
                'profile': a,
            }
            return render(request, 'student/profileupdate.html', context)
    return HttpResponseRedirect('/')


def reqlist(request):
    if request.user.is_authenticated:
        pass
    else:
        return HttpResponseRedirect('/staff/')


def Summary(request):
    if request.user.is_authenticated:
        f = Final.objects.all()
        context = {
            'summary': f,
        }
        return render(request, 'student/summary.html', context)
    else:
        return HttpResponseRedirect('/')
