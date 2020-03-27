from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView

from case.forms import CategoryForms
from case.models import Category


def category(request):
    if(request.method=='POST'):
        form = CategoryForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case.new_category')
    else:
        form = CategoryForms()
        return render(request,'new_category.html',{'form':form})

class CategoriesView(ListView):
    template_name = 'all_categories.html'
    def get_queryset(self):
        return Category.objects.all()