from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView

from residence.forms import ResidenceRegistrationForms
from residence.models import Residence


def residence_create(request):
    if request.method == 'POST':
        form = ResidenceRegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('residence.new_residence')
        else:
            print("error occurred")

    else:
        form = ResidenceRegistrationForms()
        return render(request, 'create.html', {'form': form})


def residence_dashboard(request):
    return render(request, 'dashboard.html')

class ResidencesView(ListView):
    template_name = 'all_residence.html'
    def get_queryset(self):
        return Residence.objects.all()
