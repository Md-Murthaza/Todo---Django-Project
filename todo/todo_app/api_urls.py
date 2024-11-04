from django.urls import path,include
from .views import task_list,task_detail
urlpatterns = [
    path('tasks/', task_list, name='task-list'), 
    path('tasks/<int:id>/',task_detail,name='task_detail')
    
]