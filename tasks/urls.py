

Those **must not be inside a Python file**.

Also, your current project is using `hangarin/urls.py` directly, so `tasks/urls.py` isn't currently being used. Still, we should clean it before committing so the project stays organized.

### Step 3 — Replace `tasks/urls.py`

Replace the entire file with this:

:::writing{variant="document" id="62481" title="Clean tasks/urls.py"}
```python
from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "tasks/",
        views.task_list,
        name="task_list"
    ),

    path(
        "tasks/create/",
        views.create_task,
        name="create_task"
    ),

    path(
        "tasks/<int:task_id>/",
        views.task_detail,
        name="task_detail"
    ),

    path(
        "tasks/<int:task_id>/edit/",
        views.edit_task,
        name="edit_task"
    ),

    path(
        "tasks/<int:task_id>/delete/",
        views.delete_task,
        name="delete_task"
    ),

    # Notes

    path(
        "tasks/<int:task_id>/notes/add/",
        views.add_note,
        name="add_note"
    ),

    path(
        "notes/<int:note_id>/edit/",
        views.edit_note,
        name="edit_note"
    ),

    path(
        "notes/<int:note_id>/delete/",
        views.delete_note,
        name="delete_note"
    ),

    # Subtasks

    path(
        "tasks/<int:task_id>/subtasks/add/",
        views.add_subtask,
        name="add_subtask"
    ),

    path(
        "subtasks/<int:subtask_id>/toggle/",
        views.toggle_subtask,
        name="toggle_subtask"
    ),

    path(
        "subtasks/<int:subtask_id>/edit/",
        views.edit_subtask,
        name="edit_subtask"
    ),

    path(
        "subtasks/<int:subtask_id>/delete/",
        views.delete_subtask,
        name="delete_subtask"
    ),

    # Logout

    path(
        "logout/",
        views.logout_user,
        name="logout"
    ),
]