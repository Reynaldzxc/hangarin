

from django.contrib import admin
from django.urls import path, include

from tasks.views import (
    dashboard,
    task_list,
    create_task,
    edit_task,
    delete_task,
    task_detail,
    add_note,
    edit_note,
    delete_note,
    add_subtask,
    toggle_subtask,
    delete_subtask,
    edit_subtask,
    logout_user,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("accounts/", include("allauth.urls")),

    path("", include("pwa.urls")),

    path("", dashboard, name="dashboard"),

    path("tasks/", task_list, name="task_list"),

    path("tasks/create/", create_task, name="create_task"),

    path(
        "tasks/<int:task_id>/",
        task_detail,
        name="task_detail"
    ),

    path(
        "tasks/<int:task_id>/edit/",
        edit_task,
        name="edit_task"
    ),

    path(
        "tasks/<int:task_id>/delete/",
        delete_task,
        name="delete_task"
    ),

    # Notes
    path(
        "tasks/<int:task_id>/notes/add/",
        add_note,
        name="add_note"
    ),

      path(
    "notes/<int:note_id>/edit/",
    edit_note,
    name="edit_note"
        ),
 

   
    path(
        "notes/<int:note_id>/delete/",
        delete_note,
        name="delete_note"
    ),

    # Subtasks
    path(
        "tasks/<int:task_id>/subtasks/add/",
        add_subtask,
        name="add_subtask"
    ),

    path(
        "subtasks/<int:subtask_id>/toggle/",
        toggle_subtask,
        name="toggle_subtask"
    ),

    path(
        "subtasks/<int:subtask_id>/delete/",
        delete_subtask,
        name="delete_subtask"
    ),

    path(
    "subtasks/<int:subtask_id>/delete/",
    delete_subtask,
    name="delete_subtask"
    ),  

    path(
    "subtasks/<int:subtask_id>/edit/",
    edit_subtask,
    name="edit_subtask"
    ),




   

    path("logout/", logout_user, name="logout_user"),
]