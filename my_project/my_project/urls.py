"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from operations.views import sample
from operations.views import demo
from operations.views import student_info
from operations.views import add
from operations.views import sub
from operations.views import mul
from operations.views import div
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',sample),
    path('info/',demo),
    path('student_info',student_info),
    path('addition/',add),
    path('subtraction/',sub),
    path('multiplication/',mul),
    path('division/',div)
]
