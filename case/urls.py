from django import  urls
from django.urls import path
from case.views import CategoriesView
from case import views

urlpatterns = [
    path('new_category', views.category, name='case.new_category'),
    path('all_categories', CategoriesView.as_view(), name='case.all_categories'),
]

