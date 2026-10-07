

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import logout

from .models import Task, Note, Subtask
from .forms import TaskForm


def dashboard(request):
    total_tasks = Task.objects.count()
    pending_tasks = Task.objects.filter(status="Pending").count()
    completed_tasks = Task.objects.filter(status="Completed").count()
    in_progress_tasks = Task.objects.filter(status="In Progress").count()

    context = {
        "total_tasks": total_tasks,
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks,
        "in_progress_tasks": in_progress_tasks,
    }

    return render(request, "tasks/dashboard.html", context)


def task_list(request):
    tasks = Task.objects.all()

    paginator = Paginator(tasks, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "tasks": page_obj,
        "page_obj": page_obj,
    }

    return render(request, "tasks/task_list.html", context)


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/task_form.html", context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    context = {
        "form": form,
        "task": task,
    }

    return render(request, "tasks/task_form.html", context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    context = {
        "task": task,
    }

    return render(request, "tasks/task_confirm_delete.html", context)


# =========================================================
# TASK DETAILS
# =========================================================

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    notes = Note.objects.filter(task=task).order_by("-created_at")
    subtasks = Subtask.objects.filter(parent_task=task).order_by("created_at")

    context = {
        "task": task,
        "notes": notes,
        "subtasks": subtasks,
    }

    return render(request, "tasks/task_detail.html", context)


# =========================================================
# NOTES
# =========================================================

def add_note(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Note.objects.create(
                task=task,
                content=content
            )

    return redirect("task_detail", task_id=task.id)


def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            note.content = content
            note.save()

            return redirect(
                "task_detail",
                task_id=note.task.id
            )

    context = {
        "note": note,
    }

    return render(
        request,
        "tasks/edit_note.html",
        context
    )


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    task_id = note.task.id

    if request.method == "POST":
        note.delete()

    return redirect("task_detail", task_id=task_id)


# =========================================================
# SUBTASKS
# =========================================================

def add_subtask(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Subtask.objects.create(
                parent_task=task,
                title=title
            )

    return redirect("task_detail", task_id=task.id)


def edit_subtask(request, subtask_id):
    subtask = get_object_or_404(Subtask, id=subtask_id)

    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            subtask.title = title
            subtask.save()

            return redirect(
                "task_detail",
                task_id=subtask.parent_task.id
            )

    context = {
        "subtask": subtask,
    }

    return render(
        request,
        "tasks/edit_subtask.html",
        context
    )


def toggle_subtask(request, subtask_id):
    subtask = get_object_or_404(Subtask, id=subtask_id)

    if request.method == "POST":

        if subtask.status == "Completed":
            subtask.status = "Pending"
        else:
            subtask.status = "Completed"

        subtask.save()

    return redirect(
        "task_detail",
        task_id=subtask.parent_task.id
    )


def delete_subtask(request, subtask_id):
    subtask = get_object_or_404(Subtask, id=subtask_id)

    task_id = subtask.parent_task.id

    if request.method == "POST":
        subtask.delete()

    return redirect(
        "task_detail",
        task_id=task_id
    )


# =========================================================
# LOGOUT
# =========================================================

def logout_user(request):
    logout(request)

    return redirect("account_login")

