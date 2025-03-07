"""
URL configuration for ristek_quiz_platform project.

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
from quizapp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name="home"),
    path('about', views.AboutView.as_view(), name="about"),
    path('contact', views.ContactView.as_view(), name="contact"),
    path('create', views.CreateView.as_view(), name="create_quiz"),
    path('update/<int:pk>', views.UpdateView.as_view(), name="update_quiz"),
    path('delete/<int:pk>', views.DeleteView.as_view(), name="delete_quiz")
]
