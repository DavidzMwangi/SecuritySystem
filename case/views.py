from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView

from case.forms import CategoryForms, CaseForm
from case.models import Category, Case


def category(request):
    if (request.method == 'POST'):
        form = CategoryForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case.new_category')
    else:
        form = CategoryForms()
        return render(request, 'new_category.html', {'form': form})


class CategoriesView(ListView):
    template_name = 'all_categories.html'

    def get_queryset(self):
        return Category.objects.all()


def newCase(request):
    if (request.method == 'POST'):
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            new_case = form.save(commit=False)
            new_case.user = request.user
            new_case.save()
            return redirect('case.new_case')
        else:
            print("An Error occurred")

    else:
        form = CaseForm()
        return render(request, 'new_case.html', {'form': form})


class CaseView(ListView):
    template_name = 'all_cases.html'

    def get_queryset(self):
        return Case.objects.all()


class UserCasesView(ListView):
    template_name = 'all_cases.html'

    def get_queryset(self):
        return Case.objects.filter(user=self.request.user)
