from django.contrib import admin

# Register your models here.
from case.models import Category, Case

admin.site.register(Category)
admin.site.register(Case)