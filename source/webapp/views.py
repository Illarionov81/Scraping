from celery import current_app
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from webapp.tasks import parse_all_files, get_company_data, DIR
from webapp.utils import get_companies_data, get_files


class CompanyData(View):
    def get(self, *args, **kwargs):
        context = {
            'company': get_companies_data(),
            'files': get_files(DIR)
        }
        return render(self.request, 'index.html', context=context)


class GetFiles(View):
    def get(self, *args, **kwargs):
        context = {'head': "Scraping data from sites"}
        task = get_company_data.delay()
        context['task_id'] = task.id
        return render(self.request, 'task_result.html', context=context)


class SaveInDataBase(View):
    def get(self, *args, **kwargs):
        context = {'head': "Saving data from file into db"}
        task = parse_all_files.delay()
        context['task_id'] = task.id
        return render(self.request, 'task_result.html', context=context)


class TaskView(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}
        return JsonResponse(response_data)
