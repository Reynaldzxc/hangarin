
from django.contrib import admin
from django.urls import path, include

from tasks.views import (
dashboard,
task_list,
create_task,
edit_task,
delete_task,
logout_user,
)

urlpatterns = [
path('admin/', admin.site.urls),


path('accounts/', include('allauth.urls')),

path('', include('pwa.urls')),

path('', dashboard, name='dashboard'),
path('tasks/', task_list, name='task_list'),
path('tasks/create/', create_task, name='create_task'),
path('tasks/<int:task_id>/edit/', edit_task, name='edit_task'),
path('tasks/<int:task_id>/delete/', delete_task, name='delete_task'),

path('logout/', logout_user, name='logout_user'),


]
