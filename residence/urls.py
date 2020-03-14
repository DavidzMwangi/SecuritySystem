from django.urls import path

from . import views

urlpatterns = [
        path('dashboard', views.residence_dashboard, name='residence.dashboard'),
        path('new_residence', views.residence_create, name='residence.new_residence')
]