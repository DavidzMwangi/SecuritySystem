from django.urls import path

from . import views
urlpatterns = [
        path('welcome', views.index, name='welcome'),
        path('', views.index, name='index'),
        path('admin/dashboard', views.admin_dashboard, name='admin.dashboard'),
        path('admin/register', views.admin_register, name='admin.register'),
        path('student/register', views.student_register, name='student.register'),
        path('student/dashboard', views.student_dashboard,name='student.dashboard')
]
