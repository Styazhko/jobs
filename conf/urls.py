"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from accounts.views import Register
from jobs.views import index_view, company_view, vacancy_view, vacancies_view, vacancies_cat_view, vacancies_send_view, \
    mycompany_start_view, mycompany_create_view, mycompany_view, mycompany_vacancies_view, \
    mycompany_vacancies_create_view, mycompany_vacancy_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('vacancies/cat/<str:code>/', vacancies_cat_view, name='vacancies_cat'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('companies/<int:id>/', company_view, name='company'),
    path('vacancies/<int:id>/', vacancy_view, name='vacancy'),
    path('vacancies/<int:id>/send/', vacancies_send_view, name='vacancies_send'),
    path('mycompany/start/', mycompany_start_view, name='mycompany_start'),
    path('mycompany/create/', mycompany_create_view, name='mycompany_create'),
    path('mycompany/', mycompany_view, name='mycompany'),
    path('mycompany/vacancies/', mycompany_vacancies_view, name='mycompany_vacancies'),
    path('mycompany/vacancies/create/', mycompany_vacancies_create_view, name='mycompany_vacancies_create'),
    path('mycompany/vacancies/<int:id>/', mycompany_vacancy_view, name='mycompany_vacancy'),
    # path('login', LoginFormView.as_view(), name='login'),
    path('register/', Register.as_view()),
]
