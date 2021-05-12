from django.urls import path

from webapp.views import Data

app_name = 'webapp'

urlpatterns = [
    path('', Data.as_view(), name='data'),

 ]