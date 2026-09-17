
from django.contrib import admin
from django.urls import path
from tasks.views import dashboard, task_list, create_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name ='dashboard'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', create_task, name='create_task'),
]
