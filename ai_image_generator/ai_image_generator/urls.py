"""ai_image_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from chatgpt_connector.views import *
from accounts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('generator/', generator, name='generator'),
    path('loading/', loading, name='loading'),
    path('result/', result, name='result'),
    
    # accounts
    path('signup/', signup, name='signup'),
    path('accounts/', include('allauth.urls')),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]