from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Studentinfo


class AddUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}), label='Confirm Password(again)')

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        labels = {'email': 'Email', 'username': 'Enrollment Number'}
        widgets = {'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
                   'username': forms.TextInput(attrs={'placeholder': 'Addmission Number', 'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
                   }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control', 'id': 'passwd'}))

    class Meta:
        model = User
        fields = '__all__'


class UpdateProfileForm(forms.ModelForm):
    roll = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Roll Number', 'class': 'form-control'}))
    year = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Year', 'class': 'form-control'}))
    sem = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Semester', 'class': 'form-control'}))
    branch = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Branch', 'class': 'form-control'}))

    class Meta:
        model = Studentinfo
        fields = ['roll', 'year']
        # fields = ['roll']
