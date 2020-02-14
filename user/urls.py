from django.urls import path

from . import views

urlpatterns = [
        path('welcome', views.index, name='welcome'),
        path('', views.index, name='index')
]
