"""securitysystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from securitysystem import settings
from user.views import register_view, login_view, user_logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls'), name='user'),
    path('residence/', include('residence.urls'), name='residence'),
    path('case/', include('case.urls'), name='case'),
    path('', TemplateView.as_view(template_name='login.html')),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', user_logout, name='logout')

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
