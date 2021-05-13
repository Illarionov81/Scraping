from django.shortcuts import render
from django.views.generic.base import View

from webapp.query import parse_all_files
from webapp.utils import get_company_data


class CompanyData(View):
    def get(self, *args, **kwargs):
        name = self.request.GET.get('data')
        if name == 'Get Data':
            get_company_data()
        if name == 'Save Data':
            parse_all_files()
        return render(self.request, 'base.html')

    def post(self, *args, **kwargs):
        name = self.request.POST.get('data')
        if name == 'Get Data':
            get_company_data()
        if name == 'Save Data':
            parse_all_files()
        return render(self.request, 'base.html')
