from django.urls import path

from . import views
from .views import ResidencesView

urlpatterns = [
        path('dashboard', views.residence_dashboard, name='residence.dashboard'),
        path('new_residence', views.residence_create, name='residence.new_residence'),
        path('all_residences', ResidencesView.as_view(), name='residence.all_residences')
]