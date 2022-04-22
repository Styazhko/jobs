from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest


def index_view(request: WSGIRequest):
    return render(request, 'index.html')


def vacancies_view(request: WSGIRequest, specialties):
    return render(request, 'vacancies.html')


def vacancy_view(request: WSGIRequest, id):
    return render(request, 'vacancy.html')


def company_view(request: WSGIRequest):
    return render(request, 'company.html')


# def company_create_view(request: WSGIRequest):
#     return render(request, 'company_create.html')
#
#
# def company_edit_view(request: WSGIRequest):
#     return render(request, 'company_edit.html')
#
#





