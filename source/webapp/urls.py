from django.urls import path

from webapp.views import CompanyData

app_name = 'webapp'

urlpatterns = [
    path('', CompanyData.as_view(), name='data'),

 ]