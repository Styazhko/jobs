from django.core.management.base import BaseCommand
from jobs.data import specialties, companies, jobs
from jobs.models import Specialty, Vacancy, Company


class Command(BaseCommand):


    def handle(self, *args, **options):
        for i in specialties:
            specialty = Specialty.objects.create(code = i['code'], title = i['title'])
        for j in companies:
            company = Company.objects.create(name = j['title'], logo = j['logo'], employee_count = j['employee_count'], description = j['description'])
        for k in jobs:
            vacancy = Vacancy.objects.create(title = k['title'], specialty = k['specialty'], company = k['company'], salary_min = k['salary_from'], salary_max = k['salary_to'], published_at = k['posted'], skills = k['skills'], description = k['description'])
