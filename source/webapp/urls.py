from django.urls import path

from webapp.views import CompanyData, TaskView, SaveInDataBase, GetFiles

app_name = 'webapp'

urlpatterns = [
    path('', CompanyData.as_view(), name='data'),
    path('get-files/', GetFiles.as_view(), name='get_files'),
    path('save-in-base/', SaveInDataBase.as_view(), name='Save_in_base'),
    path('task/<str:task_id>/', TaskView.as_view(), name='task'),
 ]
