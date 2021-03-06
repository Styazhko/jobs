from django.shortcuts import render
from django.http import Http404
from django.core.handlers.wsgi import WSGIRequest
from jobs.models import Vacancy, Specialty, Company
from django.db.models import Count


def index_view(request: WSGIRequest):
    specialies = Specialty.objects.annotate(vacancies_count=Count('vacancies'))
    companies = Company.objects.annotate(vacancies_count=Count('vacancies'))
    return render(request, 'index.html', context={
        'specialies': specialies,
        'companies': companies,
    })


def vacancies_view(request: WSGIRequest):
    specialies = Specialty.objects.all()
    companies = Company.objects.all()
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies.html', context={
        'specialies': specialies,
        'companies': companies,
        'vacancies': vacancies,
    })


def vacancies_cat_view(request: WSGIRequest, code):
    try:
        specialies = Specialty.objects.get(code=code)
    except Specialty.DoesNotExist:
        raise Http404
    return render(request, 'vacancies_cat.html', context={
        'specialies': specialies,
        'vacancies': Vacancy.objects.all(),
    })


def vacancy_view(request: WSGIRequest, id):
    try:
        vacancies = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        raise Http404
    return render(request, 'vacancy.html', context={
        'vacancies': vacancies,
    })


def company_view(request: WSGIRequest, id):
    try:
        companies = Company.objects.get(id=id)
    except Company.DoesNotExist:
        raise Http404
    try:
        vacancies = Vacancy.objects.get(company=id)
    except Vacancy.DoesNotExist:
        vacancies = None
    return render(request, 'company.html', context={
        'companies': companies,
        'vacancies': vacancies,
    })


def vacancies_send_view(request: WSGIRequest, id):
    try:
        vacancies = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        raise Http404
    return render(request, 'sent.html', context={
        'vacancies': vacancies,
    })


def mycompany_start_view(request: WSGIRequest):
    return render(request, 'company-create.html')


def mycompany_create_view(request: WSGIRequest):
    return render(request, 'company-edit.html')


def mycompany_view(request: WSGIRequest):
    return render(request, 'company-edit.html')


def mycompany_vacancies_view(request: WSGIRequest):
    return render(request, 'vacancy-list.html')


def mycompany_vacancies_create_view(request: WSGIRequest):
    return render(request, 'vacancy-edit.html')


def mycompany_vacancy_view(request: WSGIRequest, id):
    return render(request, 'vacancy-edit.html')


def login_view(request: WSGIRequest):
    return render(request, 'login.html')


def register_view(request: WSGIRequest):
    return render(request, 'register.html')

