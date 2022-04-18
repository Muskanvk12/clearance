"""clearance1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views as s1
from teacher import views as s2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', s1.UserSignUp, name='signup'),
    path('', s1.HomePage, name='homepage'),
    path('login/', s1.UserLogin, name='login'),
    path('profile/', s1.UserProfile, name='profile'),
    path('logout/', s1.UserLogout, name='logout'),
    path('staff/', s2.StaffLogin, name='stafflogin'),
    path('staff/profile/', s2.StaffProfile, name='staffprofile'),
    path('staff/logout', s2.StaffLogout, name='stafflogout'),
    path('profile/list', s1.sublist, name='list'),
    path('getClearance/<int:userid>', s1.getClearance, name='getclear'),
    path('profile/update/', s1.UpdateProfile, name='update'),
    path('staff/profile/list', s2.ViewRequest, name='reqlist'),
    path('staff/profile/list/active/<int:userid>', s2.activate, name='activate'),
    path('staff/profile/list/reject/<int:userid>', s2.reject, name='reject'),
    path('profile/summary/', s1.Summary, name='summary')
]
