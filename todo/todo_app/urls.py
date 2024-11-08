"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path,include
from . views import *

urlpatterns = [
    path('viewtasks/',view_tasks,name='view_tasks'),
    path('addtask/',add_task,name='add_task'),
    path('edittask/<int:task_id>/',edit_task,name='edit_task'),
    path('deletetask/<int:task_id>/',delete_task,name='delete_task'),

    ###login and register urls

    path('login/',login_page,name='login_page'),
    path('',register,name='register'),
    path('logout/',logout_page,name='logout_page')

   
    

   
   
]
