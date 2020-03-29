from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy

from user.forms import *
from user.models import Admin


@login_required
def index(request):
    return render(request, 'student/dashboard.html')


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return render(request,'login.html')

    else:
        return reverse_lazy('login')


def register_view(request):
    if (request.method == 'POST'):
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # save user depending on if the user type
            user = authenticate(username=username, password=password)
            login(request, user)

            # 0-admin 1-student 2-residence
            if (form.cleaned_data.get('user_type') == 0):
                return redirect('admin.register')
            elif (form.cleaned_data.get('user_type') == 1):
                return redirect('student.register')
            elif (form.cleaned_data.get('user_type') == 2):
                return reverse_lazy('welcome')
            else:
                return reverse_lazy('welcome')


        else:
            print("error")
            print(form.errors)

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def login_view(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == 0:
                return redirect('admin.dashboard')

            elif user.user_type == 1:
                return redirect('student.dashboard')
            else:
                print("joijoi")
        else:
            return render(request, 'login.html', {'error': 'The user does not exist, please register'})


    else:

        return render(request, 'login.html')


def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


@login_required
def admin_register(request):
    if request.method == 'POST':
        access_level = request.POST.get('access_level')
        current_user = request.user
        admin = Admin()
        admin.access_level = access_level
        admin.user = current_user
        admin.save()

        return reverse_lazy('welcome')
    else:
        return render(request, 'admin/register.html')


@login_required
def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.user = request.user
            new_student.save()

        return redirect('welcome')
    else:
        form = StudentRegisterForm()
        return render(request, 'student/register.html', {'form': form})


@login_required
def student_dashboard(request):
    if request.method == 'GET':
        return render(request, 'student/dashboard.html')
    else:
        return redirect('welcome')
