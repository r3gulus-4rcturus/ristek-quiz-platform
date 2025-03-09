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
    path('create', views.CreateQuiz.as_view(), name="create_quiz"),
    path('view/<int:pk>', views.ViewQuiz.as_view(), name="view_quiz"),
    path('update/<int:pk>', views.UpdateQuiz.as_view(), name="update_quiz"),
<<<<<<< HEAD
    path('delete/<int:pk>', views.DeleteQuiz.as_view(), name="delete_quiz"),
    path('view/<int:pk_tryout>/add_question', views.AddQuestion.as_view(), name="add_question"),
    path('view/<int:pk_tryout>/update_question/<int:pk_question>', views.UpdateQuestion.as_view(), name="update_question"),
    path('view/<int:pk_tryout>/delete_question/<int:pk_question>', views.DeleteQuestion.as_view(), name="delete_question"),
=======
    path('delete/<int:pk>', views.DeleteQuiz.as_view(), name="delete_quiz")
>>>>>>> d4edcb778130b88afc19c4edaaeb436b985c8af6
]
