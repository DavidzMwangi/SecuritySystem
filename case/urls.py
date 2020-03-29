from django import  urls
from django.urls import path
from case.views import CategoriesView,CaseView,UserCasesView
from case import views

urlpatterns = [
    path('new_category', views.category, name='case.new_category'),
    path('all_categories', CategoriesView.as_view(), name='case.all_categories'),
    path('new_case', views.newCase, name='case.new_case'),
    path('all_cases', CaseView.as_view(), name='case.all_cases'),
    path('my_cases', UserCasesView.as_view(), name='case.my_cases')
]

