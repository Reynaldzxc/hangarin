
from django.contrib import admin
from django.urls import path
from tasks.views import dashboard, task_list, create_task, edit_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name ='dashboard'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', create_task, name='create_task'),
    path("tasks/<int:task_id>/edit/", edit_task, name="edit_task"),
    path("tasks/<int:task_id>/delete/", delete_task, name="delete_task"),
]
